#!/bin/bash
mp3="/Volumes/CARMUSIC/*"

for f in $mp3 
	do
	filename=$(basename "$f")
	directory=$(dirname "$f")
	extension="${filename##*.}"
	filename="${filename%.*}"
	#echo $extension
	if [[ $extension == "wma" ]]; then
		ffmpeg -i "$directory/$filename.$extension" -c:a libmp3lame -b:a 320k -c:d copy "$directory/$filename.mp3"
	fi
done