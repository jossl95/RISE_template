# RISE Template

This repository contains files and resources that I use to customize the formatting of my RISE slides. 
[RISE](https://github.com/damianavila/RISE) is a plug in for the jupyter environment, that allow you to instantly turn Jupyter Notebooks into an interactive slideshow.

## Customizations
I customized my RISE slides in the following ways:
* I altered global settings to not center on the middel axis and use fade transitions.
* I imported Google Fonts : `Open Sans` and `Merriweather` and overwrote default settings.
* I made template slides for: title slide, two column slides (with images), full screen image slides, end slide.

## PDF export
[`Decktape`](https://rise.readthedocs.io/en/stable/exportpdf.html#using-decktape) allows to generate an PDF export of the RISE slides. The command follow:
```bash
(npm bin)/decktape rise --size 1500x900 --chrome-path $chromium $url $outfile
```

A working example would be
``` bash
./node_modules/decktape/decktape.js rise --size 1500x900 --chrome-path\
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"\
     "http://127.0.0.1:8888/notebooks/presentation.ipynb?token=c9b0d777130038289299f26e1b3f42546acca1ae9c1e7ff4"\
     "/Users/MacbookJos/OneDrive - Universiteit Utrecht/Documents/_Library/Templates/rise-presentation/slides.pdf"
```

## TO DO
* ensure that css styles are executed automatically after presentation.ipynb is made
