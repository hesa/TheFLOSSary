#!/usr/bin/env bash
#
# Required Phyton dependencies: pylatexenc

# Make sure the script is run from the repository root:
if [ -e Contributors.py ]; then
    echo "Creating TheFLOSSary PDF file."
else
    echo "Please run this script from the repository root!"
    exit 1
fi

# Generate the input file with the list of contributors:
PYTHONPATH=$PWD python3 ./scripts/contributors-list.py > Glossaries/TheFLOSSary/contributors.tex

if hash texliveonfly 2>/dev/null; then
    cd Glossaries/TheFLOSSary/ && \
    	texliveonfly -a "-view=none -interaction=nonstopmode -synctex=1 -file-line-error" \
    	TheFLOSSary.tex && \
    	latexmk -pdf -pvc -view=none -interaction=nonstopmode -synctex=1 \
    	-file-line-error TheFLOSSary.tex $@
else
	# This is mostly a reference to remember how to call latexmk on this repository:
	cd Glossaries/TheFLOSSary/ && \
    	latexmk -pdf -pvc -view=none -interaction=nonstopmode -synctex=1 -file-line-error \
    	TheFLOSSary.tex $@
fi