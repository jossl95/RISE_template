# RISE Template

This repository contains files and resources that I use to customized formatting of RISE slides. 
[RISE](https://github.com/damianavila/RISE) is a Jupyter environment plug in, that allow you to instantly turn Jupyter Notebooks into a interactive slideshow.

## Customizations
I customized my RISE slides in the following ways:
* I altered global settings to not center on the middel axis and use fade transitions.
* I import Google Fonts : `Open Sans` and `Merriweather` and overwrite default settings.
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
     "http://127.0.0.1:8888/notebooks/template.ipynb?token=c9b0d777130038289299f26e1b3f42546acca1ae9c1e7ff4"\
     "/Users/MacbookJos/OneDrive - Universiteit Utrecht/Documents/_Library/Templates/rise-presentation/slides.pdf"
```

## TO DO
* make a bash script to automate pdf export
* reposition `div #rise-footer` to optimize for decktape export 