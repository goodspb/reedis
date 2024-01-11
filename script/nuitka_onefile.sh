#!/bin/bash

APP_NAME=Reedis

BUILD_PATH=./build

rm -rf $BUILD_PATH

python -m nuitka \
          --standalone \
          --onefile\
          --enable-plugin=pyside6\
          --macos-create-app-bundle\
          --macos-app-icon=./resource/icons/icons.icns\
          --output-dir=$BUILD_PATH\
          --assume-yes-for-download\
          --macos-app-name=$APP_NAME\
          --disable-console \
          Reedis.py

cp -R "$BUILD_PATH/Resources" "$BUILD_PATH/$APP_NAME.app/Contents/Resources"
cp "$BUILD_PATH/Info.plist" "$BUILD_PATH/$APP_NAME.app/Contents/Info.plist"
