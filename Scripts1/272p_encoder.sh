#!/bin/bash
output="/Volumes/videos/!export_temp/Jared"
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"

ffmpeg -y -i "$directory/$filename.$extension" -c:v libx264 -b:v 2m -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=480:272 -strict -2 -c:a copy  "$directory"/"$filename"_272.mp4
