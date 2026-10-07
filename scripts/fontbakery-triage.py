#!/usr/bin/env python3
"""Triage a fontbakery report: what we need to fix, what's optional, what to ignore.

Reads the GitHub-markdown report that `make test` writes and groups the
results by check across the four fonts. Each check
we've already looked at gets a verdict and the reason for it, from TRIAGE below;
anything else is listed under "Not triaged yet" so a new problem stands out.

    python3 scripts/fontbakery-triage.py                  # latest build of master
    python3 scripts/fontbakery-triage.py --branch my-pr   # latest build of a branch
    python3 scripts/fontbakery-triage.py --run 123456789  # a specific build run
    python3 scripts/fontbakery-triage.py out/fontbakery/fontbakery-report.md

Without a file, it downloads the report from the "Build font and specimen"
GitHub Actions artifact, using the GitHub CLI (`gh`, logged in).

Exits with 1 if the report has a FAIL, ERROR or FATAL, or a check that isn't
in TRIAGE, and 0 otherwise. Plain Python, no venv needed.
"""

import argparse
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, OrderedDict

REPO = "balsamiq/balsamiqsans"
WORKFLOW = "build.yaml"
ARTIFACT = "balsamiqsans-fonts"
REPORT_IN_ARTIFACT = "out/fontbakery/fontbakery-report.md"
BAD_STATUSES = {"FAIL", "ERROR", "FATAL"}

# Verdicts for the checks we've looked at, keyed by fontbakery check ID.
#   fix:      a real problem we can fix in this repo
#   optional: we could fix it, but it's low value or needs design work
#   ignore:   not a problem for this font, or not fixable here
# When a check's verdict changes, or a new one shows up, update this table.
TRIAGE = {
    "outline_direction": (
        "fix",
        "TrueType expects clockwise outer contours. The sources are drawn "
        "counter-clockwise (PostScript direction) and sources/config.yaml sets "
        "`reverseOutlineDirection: false`, so the TTFs ship that way. If nearly "
        "every glyph is listed, it's this setting, not the drawings.",
        "Set `reverseOutlineDirection: true` in sources/config.yaml (fontmake "
        "only reverses the TTFs; OTFs keep PostScript direction), rebuild, and "
        "compare with `make proof`.",
    ),
    "unreachable_glyphs": (
        "fix",
        "These glyphs are exported but no codepoint, feature or composite uses "
        "them: NULL is a leftover from old TrueType conventions, and *.001 "
        "glyphs are accidental duplicates.",
        "Untick Export on them (or delete them) in the source they come from.",
    ),
    "soft_dotted": (
        "fix",
        "The ccmp feature swaps i/j for their dotless forms only before the "
        "marks in @CombiningTopAccents, and only skips cedilla, ogonek and horn "
        "below. So i with a double grave, or with a dot below plus a top "
        "accent (Yoruba, Vietnamese), keeps its dot under the accent.",
        "In the ccmp feature of both sources, add the missing top marks "
        "(e.g. dblgravecomb) to @CombiningTopAccents and the missing marks below "
        "(e.g. dotbelowcomb, commaaccentcomb) to @CombiningNonTopAccents.",
    ),
    "overlapping_path_segments": (
        "optional",
        "Mostly zero-length segments: the same point twice in a row, as at "
        "every corner of the Regular and Italic masters. Renderers don't mind. "
        "Real overlaps (two different segments on top of each other) are "
        "listed separately, and composites inherit them from their base glyph.",
        "Tidy the real overlaps by hand in Glyphs. Removing the duplicate "
        "points needs a script that rewrites nearly every outline, so only do "
        "it together with a full `make proof` comparison.",
    ),
    "math_signs_width": (
        "optional",
        "A few math glyphs have a different advance width from the rest, so "
        "they don't line up in tabular maths. Cosmetic.",
        "Set the listed glyphs' width to the common one, keeping them centred.",
    ),
    "googlefonts/vendor_id": (
        "optional",
        "The OS/2 vendor ID isn't in Microsoft's registry. It's only "
        "attribution metadata.",
        "Register a 4-letter vendor ID for Balsamiq with Microsoft, then set "
        "openTypeOS2VendorID in both sources.",
    ),
    "googlefonts/glyphsets/shape_languages": (
        "optional",
        "Two kinds of gaps in languages the glyphsets cover: missing "
        "auxiliary letters (new glyphs to draw), and combining marks that "
        "don't attach to some base letters because those letters lack the "
        "anchor (e.g. stress accents on Cyrillic vowels, Lithuanian accented "
        "ą ų ū, Yoruba's vertical line below).",
        "Add the missing top/bottom anchors to the base glyphs listed per "
        "mark, in both sources. Draw the missing letters only if those "
        "languages matter.",
    ),
    "contour_count": (
        "ignore",
        "Fontbakery compares contour counts with typical typefaces. Balsamiq "
        "Sans is hand-drawn, so strokes often join or split differently. Only "
        "worth a look if a glyph shows up here that wasn't here before.",
        None,
    ),
    "typoascender_exceeds_Agrave": (
        "ignore",
        "Fixing it means raising typoAscender. With Use Typo Metrics on, that "
        "changes the line spacing of every app and page already using the "
        "font, Balsamiq Wireframes included, and Google Fonts doesn't want "
        "vertical metrics to change on a published family.",
        None,
    ),
    "googlefonts/metadata/unreachable_subsetting": (
        "ignore",
        "The subsets Google Fonts serves are set in METADATA.pb in the "
        "google/fonts repo, not here. Most listed codepoints are combining "
        "marks that no subset includes, and adding 'vietnamese' would need "
        "full Vietnamese coverage, which the font doesn't have.",
        None,
    ),
    "googlefonts/article/images": (
        "ignore",
        "A Google Fonts family article (an optional page on fonts.google.com) "
        "lives in the google/fonts repo, not here.",
        None,
    ),
}

VERDICT_TITLES = OrderedDict([
    ("new", "Not triaged yet: read these and add them to TRIAGE"),
    ("fix", "Fix: we need to and can"),
    ("optional", "Optional: could fix, low value or design work"),
    ("ignore", "Ignore: not a problem here, or not fixable in this repo"),
])

FONT_RE = re.compile(r"<details><summary>\[\d+\] ([^<]+)</summary>")
CHECK_RE = re.compile(
    r"<summary>\S+ <b>([A-Z]+)</b> (.*?) <a href=\"[^\"]*\">([^<]+)</a></summary>"
    r"\s*<div>(.*?)</div>\s*</details>",
    re.S,
)


def plain_text(fragment):
    text = re.sub(r"<[^>]+>", "", fragment)
    text = html.unescape(text)
    lines = [line.rstrip() for line in text.splitlines()]
    return [line for line in lines if line.strip()]


def parse_report(text):
    """Return {check_id: {"title", "statuses": {font: status}, "bodies": {font: lines}}}."""
    checks = OrderedDict()
    starts = [(m.start(), m.group(1).strip()) for m in FONT_RE.finditer(text)]
    if not starts:
        # A report on a single font, or one with only family-wide checks.
        starts = [(0, "(family)")]
    for i, (start, font) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        for m in CHECK_RE.finditer(text, start, end):
            status, title, check_id, body = m.groups()
            entry = checks.setdefault(
                check_id, {"title": title.strip(), "statuses": {}, "bodies": {}}
            )
            entry["statuses"][font] = status
            entry["bodies"][font] = plain_text(body)
    return checks, [font for _, font in starts]


def parse_summary(text):
    m = re.search(r"### Summary\s*\n\s*\|(.*)\|\s*\n\s*\|[-| ]+\|\s*\n\s*\|(.*)\|", text)
    if not m:
        return {}
    names = [re.sub(r"[^A-Z]", "", cell) for cell in m.group(1).split("|")]
    counts = [cell.strip() for cell in m.group(2).split("|")]
    return {name: count for name, count in zip(names, counts) if name}


# Short, check-specific summaries of one font's message. Each takes the
# message lines and returns a one-line finding.

def glyph_names(lines, pattern):
    seen = OrderedDict()
    for line in lines:
        m = re.match(pattern, line)
        if m:
            seen[m.group(1)] = True
    return list(seen)


def summarize_list(names, limit=12):
    shown = ", ".join(names[:limit])
    more = len(names) - limit
    return f"{shown}, and {more} more" if more > 0 else shown


def finding_outline_direction(lines):
    names = glyph_names(lines, r"\* (\S+)(?: \(U\+[0-9A-F]+\))? has a counter-clockwise")
    return f"{len(names)} glyphs with a counter-clockwise outer contour"


def finding_overlapping_path_segments(lines):
    # A segment like L<<217.0,69.0>--<217.0,69.0>> starts and ends on the same
    # point: a duplicated node. Anything else is a real overlap.
    duplicates, overlaps = OrderedDict(), OrderedDict()
    for line in lines:
        m = re.match(r"\* (\S+?)(?: \(U\+[0-9A-F]+\))?: ([LB])<(.*)> has the same", line)
        if not m:
            continue
        name, kind, points = m.groups()
        coords = re.findall(r"<(-?[\d.]+,-?[\d.]+)>", points)
        if kind == "L" and len(set(coords)) == 1:
            duplicates[name] = True
        else:
            overlaps[name] = True
    duplicates = [n for n in duplicates if n not in overlaps]
    parts = []
    if overlaps:
        parts.append(f"real overlaps in {len(overlaps)} glyphs ({summarize_list(list(overlaps))})")
    if duplicates:
        parts.append(f"only duplicate points in {len(duplicates)} more")
    return "; ".join(parts) or first_line(lines)


def finding_unreachable_glyphs(lines):
    names = [line[2:] for line in lines if line.startswith("- ")]
    return ", ".join(names)


def finding_contour_count(lines):
    names = glyph_names(lines, r"- Glyph name: (\S+)\s")
    return f"{len(names)} glyphs: {summarize_list(names)}"


def finding_math_signs_width(lines):
    common = next((l for l in lines if "most common width" in l), "")
    outliers = []
    for i, line in enumerate(lines):
        m = re.match(r"Width = (\d+):", line)
        if m and i + 1 < len(lines):
            outliers.append(f"{lines[i + 1].strip()} {m.group(1)}")
    m = re.search(r"most common width is (\d+)", common)
    base = f"common width {m.group(1)}; " if m else ""
    return base + ", ".join(outliers)


def finding_soft_dotted(lines):
    m = re.search(r"following strings: (.*)", lines[0])
    return f"dot not removed in: {m.group(1)}" if m else first_line(lines)


def finding_shape_languages(lines):
    missing = OrderedDict()
    unattached = OrderedDict()  # mark -> bases it doesn't attach to
    for line in lines:
        m = re.search(r"missing from the font: (.*)", line)
        if m:
            for char in m.group(1).split(","):
                missing[char.strip()] = True
        m = re.search(r"didn't attach (\S+) to (\S+)", line)
        if m:
            unattached.setdefault(m.group(1), OrderedDict())[m.group(2)] = True
    parts = []
    if missing:
        parts.append(f"{len(missing)} missing letters ({summarize_list(list(missing), 20)})")
    for mark, bases in unattached.items():
        parts.append(f"{mark} doesn't attach to {summarize_list(list(bases))}")
    return "; ".join(parts) or first_line(lines)


def finding_unreachable_subsetting(lines):
    codepoints = [l for l in lines if re.match(r"U\+[0-9A-F]{4,6} ", l)]
    return f"{len(codepoints)} codepoints not in any declared subset"


def first_line(lines):
    for line in lines:
        text = re.sub(r"^\*?\s*\S*\s*\*\*[A-Z]+\*\*\s*", "", line).strip()
        if text and not text.startswith("[code:"):
            return text[:200]
    return ""


FINDINGS = {
    "outline_direction": finding_outline_direction,
    "overlapping_path_segments": finding_overlapping_path_segments,
    "unreachable_glyphs": finding_unreachable_glyphs,
    "contour_count": finding_contour_count,
    "math_signs_width": finding_math_signs_width,
    "soft_dotted": finding_soft_dotted,
    "googlefonts/glyphsets/shape_languages": finding_shape_languages,
    "googlefonts/metadata/unreachable_subsetting": finding_unreachable_subsetting,
}


def font_label(fonts, all_fonts):
    if len(all_fonts) > 1 and set(fonts) == set(all_fonts):
        return f"all {len(all_fonts)} fonts"
    return ", ".join(f.replace("BalsamiqSans-", "").replace(".ttf", "") for f in fonts)


def print_check(check_id, entry, all_fonts, verdict):
    statuses = Counter(entry["statuses"].values())
    status = "/".join(sorted(statuses))
    print(f"  {check_id}  [{status}]  {entry['title']}")
    summarize = FINDINGS.get(check_id, first_line)
    # Fonts with the same finding are shown together.
    by_finding = OrderedDict()
    for font, lines in entry["bodies"].items():
        by_finding.setdefault(summarize(lines), []).append(font)
    for finding, fonts in by_finding.items():
        print(f"      {font_label(fonts, all_fonts)}: {finding}")
    if check_id in TRIAGE:
        _, why, how = TRIAGE[check_id]
        print(f"      Why: {why}")
        if how:
            print(f"      Fix: {how}")
    print()


def gh(*args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"gh {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout


def find_run(branch):
    """Latest completed build of the branch that still has its artifact."""
    runs = json.loads(gh(
        "run", "list", "-R", REPO, "--workflow", WORKFLOW, "--branch", branch,
        "--status", "completed", "-L", "10",
        "--json", "databaseId,displayTitle,createdAt,conclusion",
    ))
    for run in runs:
        artifacts = json.loads(gh(
            "api", f"repos/{REPO}/actions/runs/{run['databaseId']}/artifacts",
        ))["artifacts"]
        if any(a["name"] == ARTIFACT and not a["expired"] for a in artifacts):
            return run
    sys.exit(f"No recent build of {branch} in {REPO} has a {ARTIFACT} artifact.")


def download_report(run_id):
    """Download the run's artifact and return the report's text."""
    with tempfile.TemporaryDirectory() as tmp:
        gh("run", "download", str(run_id), "-R", REPO, "-n", ARTIFACT, "-D", tmp)
        path = os.path.join(tmp, REPORT_IN_ARTIFACT)
        if not os.path.exists(path):
            found = glob.glob(os.path.join(tmp, "**", "fontbakery-report.md"), recursive=True)
            if not found:
                sys.exit(f"Run {run_id}'s artifact has no fontbakery report.")
            path = found[0]
        with open(path, encoding="utf-8") as f:
            return f.read()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("report", nargs="?",
                        help="a local fontbakery markdown report "
                             "(default: download it from GitHub Actions)")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--branch", default="master",
                        help="use the latest build of this branch (default: master)")
    source.add_argument("--run", type=int, help="use this GitHub Actions run ID")
    args = parser.parse_args()

    if args.report:
        with open(args.report, encoding="utf-8") as f:
            text = f.read()
        print(f"Report: {args.report}")
    else:
        if args.run:
            run_id = args.run
            print(f"Report: build run {run_id}")
        else:
            run = find_run(args.branch)
            run_id = run["databaseId"]
            print(f"Report: latest build of {args.branch}, run {run_id} "
                  f"({run['createdAt'][:10]}, {run['conclusion']}): {run['displayTitle']}")
        print(f"        https://github.com/{REPO}/actions/runs/{run_id}")
        text = download_report(run_id)
    checks, fonts = parse_report(text)
    summary = parse_summary(text)

    version = re.search(r"fontbakery version: (\S+)", text)
    if version:
        print(f"Fontbakery {version.group(1)}, fonts: {', '.join(fonts)}")
    if summary:
        print("Totals: " + ", ".join(f"{k} {v}" for k, v in summary.items() if v != "0"))
    print()

    groups = OrderedDict((v, []) for v in VERDICT_TITLES)
    has_bad_status = False
    for check_id, entry in checks.items():
        bad = BAD_STATUSES & set(entry["statuses"].values())
        has_bad_status = has_bad_status or bool(bad)
        verdict = TRIAGE.get(check_id, ("new",))[0]
        # A FAIL or worse always needs a look, even on a check we used to ignore.
        if bad and verdict != "fix":
            verdict = "new"
        groups[verdict].append(check_id)

    for verdict, title in VERDICT_TITLES.items():
        if not groups[verdict]:
            continue
        print(f"== {title} ({len(groups[verdict])})")
        print()
        for check_id in groups[verdict]:
            print_check(check_id, checks[check_id], fonts, verdict)

    if not checks:
        print("No results listed in the report (only WARN and worse are included).")

    return 1 if has_bad_status or groups["new"] else 0


if __name__ == "__main__":
    sys.exit(main())
