#!/bin/bash
output="/Users/chrissmith/Desktop/POD_VIDEOS_AWS/Finished/"
input="/Volumes/videos/!export_temp/Jaede/temp/*"

for f in $input
	do
	filename=$(basename "$f")
	directory=$(dirname "$f")
	extension="${filename##*.}"
	filename="${filename%.*}"
	if [[ $filename == *"_MATCH_SOURCE"* ]]; then
	#	echo $filename
	#	newName=${filename/_MATCH_SOURCE/_720p}
	#length=$(ffmpeg -i "$directory/$filename.mp4" 2>&1 | grep "Duration" | cut -d ' ' -f 4 | sed s/,// | sed 's@\..*@@g' | awk '{ split($1, A, ":"); split(A[3], B, "."); print 3600*A[1] + 60*A[2] + B[1] }')
	#echo $length
	#bitRate=$(( (802816 / $length) - 320))k
	#echo $bitRaten
	#ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v $bitRate -preset veryslow -profile:v high -level 4.0 -vf unsharp -vf scale=1280:720 -strict -2 -c:a copy "$directory"/"$newName".mp4 -y
	newName=${filename/_MATCH_SOURCE/_360p}
	ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a copy "$directory"/"$newName".mp4
	fi
done
