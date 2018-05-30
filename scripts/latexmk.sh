#!/usr/bin/env bash
#
# This is mostly a reference to remember how to call latexmk on this repository:
latexmk -pdf -pvc -view=none -interaction=nonstopmode -synctex=1 -file-line-error $@
