#!/bin/bash
input=(/Volumes/videos/videos/secret_weapon/sw_05_04_2017/Masters/*)
#filename=$(basename "$1")
#directory=$(dirname "$1")
#extension="${filename##*.}"
#filename="${filename%.*}"

for f in "${input[@]}"
 do
    filename=$(basename "$f")
    directory=$(dirname "$f")
    extension="${filename##*.}"
    filename="${filename%.*}"
echo -e "Encoding AVI for: " "$filename"
ffmpeg -y -i "$directory/$filename.$extension" -c:v libxvid -b:v 500k -vf unsharp -vf scale=480:272 -c:a libmp3lame  "$directory"/"$filename".avi
echo -e "Encoding MP4 for: " "$filename"
ffmpeg -y -i "$directory/$filename.$extension" -c:v libx264 -b:v 2m -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=480:272 -strict -2 -c:a copy -pix_fmt yuv420p "$directory"/"$filename"_272.mp4
done