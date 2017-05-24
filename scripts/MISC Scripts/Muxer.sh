#!/bin/bash
INPUT=/Volumes/Studies\ Weekly\ 7/mixes/*
for f in $INPUT
	do
	filename=$(basename "$f")
	extension="${filename##*.}"
    echo $extension
	#if [[ $extension == "mp4" ]]
    #then
	#	audio=${filename::-4}
	#	echo $audio

	#newName=${filename/_MATCH_SOURCE/_360p}
	#ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a copy "$directory"/"$newName".mp4
	#fi
done
