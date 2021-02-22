#!/bin/bash

decktape="./node_modules/decktape/decktape.js"
url="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
filename="/Users/MacbookJos/OneDrive - Universiteit Utrecht/Documents/_Library/Templates/rise-presentation/slides.pdf"
jupyter="http://127.0.0.1:8888/notebooks/template.ipynb?token=c9b0d777130038289299f26e1b3f42546acca1ae9c1e7ff4"

cd /Users/MacbookJos
$decktape rise --size 1500x900 $jupyter --chrome-path $url $filename
cd "/Users/MacbookJos/OneDrive - Universiteit Utrecht/Documents/_Library/Templates/rise-presentation"



./node_modules/decktape/decktape.js rise --size 1500x900 --chrome-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "http://127.0.0.1:8888/notebooks/template.ipynb?token=c9b0d777130038289299f26e1b3f42546acca1ae9c1e7ff4" "/Users/MacbookJos/OneDrive - Universiteit Utrecht/Documents/_Library/Templates/rise-presentation/slides.pdf"