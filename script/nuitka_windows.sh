#!/bin/bash


rm -rf ./build

python -m nuitka --standalone --enable-plugin=pyside6 --output-dir=./build --windows-icon-from-ico=./resource/icons/icons.ico --disable-console Reedis.py