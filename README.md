# The Balsamiq Sans Font

Balsamiq Sans is the handwritten font created for [Balsamiq Wireframes](https://balsamiq.com/wireframes/) and has been in use since version 2.1.

For more information, visit the  https://balsamiq.com/givingback/opensource/font/

## Webfont
To use Balsamiq Sans font as a webfont, balsamiqsans.css is included.

### How to use
1. @import
You can import the file into your stylesheet as follows:

```
@import url("webfonts/balsamiqsans.css");
```

NOTE: The directory where the stylesheet is placed.

2. Link a stylesheet
You may also link to the stylesheet in the <head> of the HTML document:

```
<link rel="stylesheet" type="text/css" href="webfonts/balsamiqsans.css">
```

NOTE: The directory where the stylesheet is placed.

3. Use the font name to style elements

Then you may use it to style elements:

```
body {
  font-family: 'BalsamiqSans', sans-serif;
  font-weight: normal;
}
```

## Maintenance

When working on the font, you can commit changes to a new branch and open a Pull Request. GitHub Actions will automatically run the build steps to produce fonts, so you can see what would later land on Google Fonts. After each commit and push, you'll see a "Build font and specimen" action at the bottom of the Pull Request. Click on it to see what happened during the build (check the section called "Check with fontbakery" to see what the quality assurance tool used by Google Fonts found), then click on "Summary" to see any "artifacts" (Zip-files with fonts) produced if there were no errors during building.

### How to Make a Release

Google Fonts uses Github Releases to manage font families. If you feel your font project has hit a milestone, you must create a new release for it. In order to do this, go to the releases page and hit the "Draft a new release button". You must provide a tag number and title which can only be a decimal number e.g 0.100, 1.000 etc. For the body text, mention what has changed since the last release. Once you are done, hit the "Publish release" button. Here is an example which fulfills the requirements, https://github.com/m4rc1e/test-ufr-family/releases/tag/2.019. For more info regarding Github release, please see the official Github Release documentation. Please note that Github Actions must be able to build the fonts before you can make a release. Once you have made a release, the fonts and tests assets will be attached to the release automatically. This may take a while since the fonts and tests will be built from scratch so please be patient.

## License

See https://github.com/balsamiq/balsamiqsans/blob/master/OFL.txt
