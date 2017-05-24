#!/bin/bash
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
newName=${filename/_MATCH_SOURCE/_272}
ffmpeg -i "$directory/$filename.mp4" -c:v libx264 -b:v 2m -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=480:272 -strict -2 -c:a copy "$directory"/"$newName".mp4