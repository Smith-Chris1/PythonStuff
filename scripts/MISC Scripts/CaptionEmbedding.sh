#!/bin/bash
output="/Users/chrissmith/Desktop/POD_VIDEOS_AWS/Finished/"
input="/Users/chrissmith/Desktop/POD_VIDEOS_AWS/*"

for f in $input
	do
	filename=$(basename "$f")
	directory=$(dirname "$f")
	extension="${filename##*.}"
	filename="${filename%.*}"
	if [ $extension = 'mp4' ]; then
		echo $filename
		ffmpeg -y -i "$directory/$filename.$extension" -i "$directory/$filename".srt -codec copy -c:s mov_text -metadata:s:s:0 language=eng "$output"/"$filename".mp4
	fi
done
