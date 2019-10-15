## Fontbakery report

Fontbakery version: 0.7.12

<details>
<summary><b>[18] Balsamiq-SansBold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
* 🔥 **FAIL** Style name used in "Balsamiq-SansBold.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00A0 (NO-BREAK SPACE), 0x00AD (SOFT HYPHEN), 0x2074 (SUPERSCRIPT FOUR) and 0x2215 (DIVISION SLASH) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 1 (MACINTOSH) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]

</details>
<details>
<summary>🔥 <b>FAIL:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
* 🔥 **FAIL** A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry. Currently accepted licenses are Apache: 'http://www.apache.org/licenses/LICENSE-2.0' or Open Font License: 'http://scripts.sil.org/OFL'
For a small set of legacy families the Ubuntu Font License 'https://www.ubuntu.com/legal/terms-and-policies/font-licence' may be acceptable as well.
When in doubt, please choose OFL for new font projects. [code: no-license-found]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)
* 🔥 **FAIL** Name table record with key = (1, 0, 0, 5) has trailing spaces that must be removed: 'Version 001.000 '
* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 5) has trailing spaces that must be removed: 'Version 001.000 '

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1049, but got 993 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 370, but got 263 instead [code: descent]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)
* 🔥 **FAIL** Whitespace glyphs missing for the following codepoints: 0x00A0. [code: missing-whitespace-glyphs]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)
* 🔥 **FAIL** Some namerecords with ID=10 (NameID.DESCRIPTION) containing copyright info should be removed (perhaps these were added by a longstanding FontLab Studio 5.x bug that copied copyright notices to them.) [code: copyright-on-description]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
* 🔥 **FAIL** This font lacks a digital signature (DSIG table). Some applications may require one (even if only a dummy placeholder) in order to work properly. You can add a DSIG table by running the `gftools fix-dsig` script. [code: lacks-signature]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value '2ttf' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
* ⚠ **WARN** The gasp range 0xFFFF value 0x02 should be set to 0x0F. [code: unset-flags]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (1000) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: ucircumflex	Contours detected: 3	Expected: 2
Glyph name: dcroat	Contours detected: 3	Expected: 2
Glyph name: gcommaaccent	Contours detected: 2	Expected: 3 or 4
Glyph name: Hbar	Contours detected: 1	Expected: 2
Glyph name: hbar	Contours detected: 3	Expected: 1
Glyph name: Jcircumflex	Contours detected: 1	Expected: 2
Glyph name: ncaron	Contours detected: 1	Expected: 2
Glyph name: napostrophe	Contours detected: 1	Expected: 2
Glyph name: Sacute	Contours detected: 3	Expected: 2
Glyph name: Scaron	Contours detected: 3	Expected: 2
Glyph name: scaron	Contours detected: 4	Expected: 2
Glyph name: tcaron	Contours detected: 1	Expected: 2
Glyph name: uhungarumlaut	Contours detected: 1	Expected: 3
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: Zdotaccent	Contours detected: 3	Expected: 2
Glyph name: Zcaron	Contours detected: 3	Expected: 2
Glyph name: uni0194	Contours detected: 1	Expected: 2
Glyph name: uni019D	Contours detected: 2	Expected: 1
Glyph name: uni01C3	Contours detected: 1	Expected: 2
Glyph name: uni01C4	Contours detected: 2	Expected: 4
Glyph name: uni01C5	Contours detected: 2	Expected: 4
Glyph name: uni01D1	Contours detected: 2	Expected: 3
Glyph name: uni01D2	Contours detected: 2	Expected: 3
Glyph name: uni01D5	Contours detected: 3	Expected: 4
Glyph name: uni01D7	Contours detected: 3	Expected: 4
Glyph name: uni01D9	Contours detected: 3	Expected: 4
Glyph name: uni01DA	Contours detected: 2	Expected: 4
Glyph name: uni01DB	Contours detected: 3	Expected: 4
Glyph name: uni01DE	Contours detected: 4	Expected: 5
Glyph name: uni01E0	Contours detected: 3	Expected: 4
Glyph name: uni01E2	Contours detected: 2	Expected: 3
Glyph name: uni01E5	Contours detected: 3	Expected: 2
Glyph name: uni01EC	Contours detected: 2	Expected: 3
Glyph name: uni01ED	Contours detected: 2	Expected: 3
Glyph name: uni01F2	Contours detected: 2	Expected: 3
Glyph name: uni01F4	Contours detected: 1	Expected: 2
Glyph name: uni01F5	Contours detected: 2	Expected: 3
Glyph name: uni01F6	Contours detected: 2	Expected: 1
Glyph name: uni01F9	Contours detected: 1	Expected: 2
Glyph name: aeacute	Contours detected: 5	Expected: 4
Glyph name: oslashacute	Contours detected: 3	Expected: 4
Glyph name: Delta	Contours detected: 0	Expected: 2
Glyph name: reflexsubset	Contours detected: 1	Expected: 2
Glyph name: reflexsuperset	Contours detected: 1	Expected: 2
Glyph name: uniFB00	Contours detected: 3	Expected: 1 or 2
Glyph name: uniFB06	Contours detected: 2	Expected: 1
Glyph name: Omega	Contours detected: 3	Expected: 1
Glyph name: uni04B9	Contours detected: 2	Expected: 1
Glyph name: uni04F2	Contours detected: 2	Expected: 3
Glyph name: uni04F3	Contours detected: 1	Expected: 3
Glyph name: uni2752	Contours detected: 3	Expected: 2
Glyph name: uni275D	Contours detected: 2	Expected: 1
Glyph name: uni275E	Contours detected: 2	Expected: 1
Glyph name: uni2761	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)
* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[18] Balsamiq-SansBoldItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
* 🔥 **FAIL** Style name used in "Balsamiq-SansBoldItalic.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00A0 (NO-BREAK SPACE), 0x00AD (SOFT HYPHEN), 0x2074 (SUPERSCRIPT FOUR) and 0x2215 (DIVISION SLASH) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 1 (MACINTOSH) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]

</details>
<details>
<summary>🔥 <b>FAIL:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
* 🔥 **FAIL** A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry. Currently accepted licenses are Apache: 'http://www.apache.org/licenses/LICENSE-2.0' or Open Font License: 'http://scripts.sil.org/OFL'
For a small set of legacy families the Ubuntu Font License 'https://www.ubuntu.com/legal/terms-and-policies/font-licence' may be acceptable as well.
When in doubt, please choose OFL for new font projects. [code: no-license-found]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)
* 🔥 **FAIL** Name table record with key = (1, 0, 0, 5) has trailing spaces that must be removed: 'Version 001.000 '
* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 5) has trailing spaces that must be removed: 'Version 001.000 '

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1049, but got 993 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 370, but got 263 instead [code: descent]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)
* 🔥 **FAIL** Whitespace glyphs missing for the following codepoints: 0x00A0. [code: missing-whitespace-glyphs]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)
* 🔥 **FAIL** Some namerecords with ID=10 (NameID.DESCRIPTION) containing copyright info should be removed (perhaps these were added by a longstanding FontLab Studio 5.x bug that copied copyright notices to them.) [code: copyright-on-description]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
* 🔥 **FAIL** This font lacks a digital signature (DSIG table). Some applications may require one (even if only a dummy placeholder) in order to work properly. You can add a DSIG table by running the `gftools fix-dsig` script. [code: lacks-signature]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value '2ttf' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
* ⚠ **WARN** The gasp range 0xFFFF value 0x02 should be set to 0x0F. [code: unset-flags]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (1000) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: ucircumflex	Contours detected: 3	Expected: 2
Glyph name: dcroat	Contours detected: 3	Expected: 2
Glyph name: gcommaaccent	Contours detected: 2	Expected: 3 or 4
Glyph name: Hbar	Contours detected: 1	Expected: 2
Glyph name: hbar	Contours detected: 3	Expected: 1
Glyph name: Jcircumflex	Contours detected: 1	Expected: 2
Glyph name: ncaron	Contours detected: 1	Expected: 2
Glyph name: napostrophe	Contours detected: 1	Expected: 2
Glyph name: Sacute	Contours detected: 3	Expected: 2
Glyph name: Scaron	Contours detected: 3	Expected: 2
Glyph name: scaron	Contours detected: 4	Expected: 2
Glyph name: tcaron	Contours detected: 1	Expected: 2
Glyph name: uhungarumlaut	Contours detected: 1	Expected: 3
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: Zdotaccent	Contours detected: 3	Expected: 2
Glyph name: Zcaron	Contours detected: 3	Expected: 2
Glyph name: uni0194	Contours detected: 1	Expected: 2
Glyph name: uni019D	Contours detected: 2	Expected: 1
Glyph name: uni01C3	Contours detected: 1	Expected: 2
Glyph name: uni01C4	Contours detected: 2	Expected: 4
Glyph name: uni01C5	Contours detected: 2	Expected: 4
Glyph name: uni01D1	Contours detected: 2	Expected: 3
Glyph name: uni01D2	Contours detected: 2	Expected: 3
Glyph name: uni01D5	Contours detected: 3	Expected: 4
Glyph name: uni01D7	Contours detected: 3	Expected: 4
Glyph name: uni01D9	Contours detected: 3	Expected: 4
Glyph name: uni01DA	Contours detected: 2	Expected: 4
Glyph name: uni01DB	Contours detected: 3	Expected: 4
Glyph name: uni01DE	Contours detected: 4	Expected: 5
Glyph name: uni01E0	Contours detected: 3	Expected: 4
Glyph name: uni01E2	Contours detected: 2	Expected: 3
Glyph name: uni01E5	Contours detected: 3	Expected: 2
Glyph name: uni01EC	Contours detected: 2	Expected: 3
Glyph name: uni01ED	Contours detected: 2	Expected: 3
Glyph name: uni01F2	Contours detected: 2	Expected: 3
Glyph name: uni01F4	Contours detected: 1	Expected: 2
Glyph name: uni01F5	Contours detected: 2	Expected: 3
Glyph name: uni01F6	Contours detected: 2	Expected: 1
Glyph name: uni01F9	Contours detected: 1	Expected: 2
Glyph name: aeacute	Contours detected: 5	Expected: 4
Glyph name: oslashacute	Contours detected: 3	Expected: 4
Glyph name: Delta	Contours detected: 0	Expected: 2
Glyph name: reflexsubset	Contours detected: 1	Expected: 2
Glyph name: reflexsuperset	Contours detected: 1	Expected: 2
Glyph name: uniFB00	Contours detected: 3	Expected: 1 or 2
Glyph name: uniFB06	Contours detected: 2	Expected: 1
Glyph name: Omega	Contours detected: 3	Expected: 1
Glyph name: uni04B9	Contours detected: 2	Expected: 1
Glyph name: uni04F2	Contours detected: 2	Expected: 3
Glyph name: uni04F3	Contours detected: 1	Expected: 3
Glyph name: uni2752	Contours detected: 3	Expected: 2
Glyph name: uni275D	Contours detected: 2	Expected: 1
Glyph name: uni275E	Contours detected: 2	Expected: 1
Glyph name: uni2761	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)
* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[18] Balsamiq-SansItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
* 🔥 **FAIL** Style name used in "Balsamiq-SansItalic.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00A0 (NO-BREAK SPACE), 0x00AD (SOFT HYPHEN), 0x2074 (SUPERSCRIPT FOUR) and 0x2215 (DIVISION SLASH) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 1 (MACINTOSH) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]

</details>
<details>
<summary>🔥 <b>FAIL:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
* 🔥 **FAIL** A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry. Currently accepted licenses are Apache: 'http://www.apache.org/licenses/LICENSE-2.0' or Open Font License: 'http://scripts.sil.org/OFL'
For a small set of legacy families the Ubuntu Font License 'https://www.ubuntu.com/legal/terms-and-policies/font-licence' may be acceptable as well.
When in doubt, please choose OFL for new font projects. [code: no-license-found]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)
* 🔥 **FAIL** Name table record with key = (1, 0, 0, 5) has trailing spaces that must be removed: 'Version 001.000 '
* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 5) has trailing spaces that must be removed: 'Version 001.000 '

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1049, but got 993 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 370, but got 263 instead [code: descent]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)
* 🔥 **FAIL** Whitespace glyphs missing for the following codepoints: 0x00A0. [code: missing-whitespace-glyphs]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)
* 🔥 **FAIL** Some namerecords with ID=10 (NameID.DESCRIPTION) containing copyright info should be removed (perhaps these were added by a longstanding FontLab Studio 5.x bug that copied copyright notices to them.) [code: copyright-on-description]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
* 🔥 **FAIL** This font lacks a digital signature (DSIG table). Some applications may require one (even if only a dummy placeholder) in order to work properly. You can add a DSIG table by running the `gftools fix-dsig` script. [code: lacks-signature]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value '2ttf' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
* ⚠ **WARN** The gasp range 0xFFFF value 0x02 should be set to 0x0F. [code: unset-flags]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (1000) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: seven	Contours detected: 2	Expected: 1
Glyph name: Hbar	Contours detected: 1	Expected: 2
Glyph name: lcommaaccent	Contours detected: 3	Expected: 2
Glyph name: uni018C	Contours detected: 3	Expected: 2
Glyph name: uni0194	Contours detected: 1	Expected: 2
Glyph name: uni01D5	Contours detected: 3	Expected: 4
Glyph name: uni01D7	Contours detected: 3	Expected: 4
Glyph name: uni01D9	Contours detected: 3	Expected: 4
Glyph name: uni01DB	Contours detected: 3	Expected: 4
Glyph name: uni01DE	Contours detected: 4	Expected: 5
Glyph name: uni01E0	Contours detected: 3	Expected: 4
Glyph name: uni01F6	Contours detected: 2	Expected: 1
Glyph name: guilsinglright	Contours detected: 2	Expected: 1
Glyph name: uniFB00	Contours detected: 3	Expected: 1 or 2
Glyph name: uniFB06	Contours detected: 2	Expected: 1
Glyph name: uni04F2	Contours detected: 2	Expected: 3
Glyph name: uni04F3	Contours detected: 1	Expected: 3
Glyph name: uni2752	Contours detected: 15	Expected: 2
Glyph name: uni275B	Contours detected: 11	Expected: 1
Glyph name: uni275C	Contours detected: 7	Expected: 1
Glyph name: uni275D	Contours detected: 12	Expected: 1
Glyph name: uni275E	Contours detected: 14	Expected: 1
Glyph name: uni2761	Contours detected: 14	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)
* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[18] Balsamiq-SansRegular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
* 🔥 **FAIL** Style name used in "Balsamiq-SansRegular.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00A0 (NO-BREAK SPACE), 0x00AD (SOFT HYPHEN), 0x2074 (SUPERSCRIPT FOUR) and 0x2215 (DIVISION SLASH) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 1 (MACINTOSH) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]
* 🔥 **FAIL** License file LICENSE.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq" Must be changed to "Licensed under the Apache License, Version 2.0" [code: wrong]

</details>
<details>
<summary>🔥 <b>FAIL:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
* 🔥 **FAIL** A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry. Currently accepted licenses are Apache: 'http://www.apache.org/licenses/LICENSE-2.0' or Open Font License: 'http://scripts.sil.org/OFL'
For a small set of legacy families the Ubuntu Font License 'https://www.ubuntu.com/legal/terms-and-policies/font-licence' may be acceptable as well.
When in doubt, please choose OFL for new font projects. [code: no-license-found]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2011-2013 by Balsamiq SRL. All rights reserved." [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)
* 🔥 **FAIL** Name table record with key = (1, 0, 0, 5) has trailing spaces that must be removed: 'Version 001.000 '
* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 5) has trailing spaces that must be removed: 'Version 001.000 '

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1049, but got 993 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 370, but got 263 instead [code: descent]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)
* 🔥 **FAIL** Whitespace glyphs missing for the following codepoints: 0x00A0. [code: missing-whitespace-glyphs]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)
* 🔥 **FAIL** Some namerecords with ID=10 (NameID.DESCRIPTION) containing copyright info should be removed (perhaps these were added by a longstanding FontLab Studio 5.x bug that copied copyright notices to them.) [code: copyright-on-description]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
* 🔥 **FAIL** This font lacks a digital signature (DSIG table). Some applications may require one (even if only a dummy placeholder) in order to work properly. You can add a DSIG table by running the `gftools fix-dsig` script. [code: lacks-signature]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value '2ttf' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
* ⚠ **WARN** The gasp range 0xFFFF value 0x02 should be set to 0x0F. [code: unset-flags]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (1000) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: seven	Contours detected: 2	Expected: 1
Glyph name: Hbar	Contours detected: 1	Expected: 2
Glyph name: lcommaaccent	Contours detected: 3	Expected: 2
Glyph name: uni018C	Contours detected: 3	Expected: 2
Glyph name: uni0194	Contours detected: 1	Expected: 2
Glyph name: uni01D5	Contours detected: 3	Expected: 4
Glyph name: uni01D7	Contours detected: 3	Expected: 4
Glyph name: uni01D9	Contours detected: 3	Expected: 4
Glyph name: uni01DB	Contours detected: 3	Expected: 4
Glyph name: uni01DE	Contours detected: 4	Expected: 5
Glyph name: uni01E0	Contours detected: 3	Expected: 4
Glyph name: uni01F6	Contours detected: 2	Expected: 1
Glyph name: guilsinglright	Contours detected: 2	Expected: 1
Glyph name: uniFB00	Contours detected: 3	Expected: 1 or 2
Glyph name: uniFB06	Contours detected: 2	Expected: 1
Glyph name: uni04F2	Contours detected: 2	Expected: 3
Glyph name: uni04F3	Contours detected: 1	Expected: 3
Glyph name: uni2752	Contours detected: 15	Expected: 2
Glyph name: uni275B	Contours detected: 11	Expected: 1
Glyph name: uni275C	Contours detected: 7	Expected: 1
Glyph name: uni275D	Contours detected: 12	Expected: 1
Glyph name: uni275E	Contours detected: 14	Expected: 1
Glyph name: uni2761	Contours detected: 14	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]
* ⚠ **WARN** Name table entry ("Balsamiq Sans Font(c) 2011-2015 Michael Angeles for Balsamiq, SRLThis font is licensed under the SIL OFL license: http://scripts.sil.org/OFLReserved Font Name: Balsamiq") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)
* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 44 | 28 | 285 | 25 | 174 | 0 |
| 0% | 8% | 5% | 51% | 4% | 31% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
