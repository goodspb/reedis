#!/bin/bash

APP_PATH="../build/Reedis.app"

create-dmg \
  --volname "Reedis" \
  --background "../resource/background.png"\
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon $APP_PATH 200 190 \
  --hide-extension $APP_PATH \
  --app-drop-link 400 185 \
  "Reedis.dmg" \
  $APP_PATH