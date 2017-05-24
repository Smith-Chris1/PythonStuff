#!/bin/bash
output="/Volumes/videos/!export_temp/Jared"
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"

ffmpeg -y -i "$directory/$filename.$extension" -c:v libxvid -b:v 500k -vf unsharp -vf scale=480:272 -c:a libmp3lame  "$directory"/"$filename".avi
