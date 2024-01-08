#!/bin/bash

APP_NAME=Reedis.app
APP_PATH=./build/

create-dmg \
  --volname "Reedis Installer" \
  --background "./resource/background.png" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "$APP_NAME" 200 190 \
  --hide-extension "$APP_NAME" \
  --app-drop-link 400 185 \
  "Reedis_Installer.dmg" \
  $APP_PATH