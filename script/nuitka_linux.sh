#!/bin/bash

APP_NAME=Reedis

BUILD_PATH=./build

rm -rf $BUILD_PATH

python -m nuitka \
          --standalone \
          --enable-plugin=pyside6\
          --linux-icon=./resource/icons/icons.ico\
          --output-dir=$BUILD_PATH\
          --disable-console \
          --static-libpython=no \
          Reedis.py

