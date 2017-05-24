#!/bin/bash
output="/Volumes/videos/!export_temp/Jared"
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
if [[ $extension == "mp4" ]]
echo $directory
echo $filename
echo $extension
then
if [[ $filename == *"_Temp"* ]]
	then
	clear
	echo -e 'Currently processing:\n'$filename'\nEncoding will begin shortly.\n'
	#sleep 60
	newName=${filename/_Temp/_360p}
	ffmpeg -y -i "$directory/$filename.mp4" -i $2 -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a "$directory"/"$newName".mp4
	newName=${filename/_Temp/_720p}
	length=$(ffmpeg -i "$directory/$filename.mp4" 2>&1 | grep "Duration" | cut -d ' ' -f 4 | sed s/,// | sed 's@\..*@@g' | awk '{ split($1, A, ":"); split(A[3], B, "."); print 3600*A[1] + 60*A[2] + B[1] }')
	#echo $length
	bitRate=$(( (802816 / $length) - 320))k
	#echo $bitRaten
	ffmpeg -y -i "$directory/$filename.mp4" -i $2 -c:v libx264 -b:v $bitRate -preset veryslow -level 4.0 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a "$directory"/"$newName".mp4
else	 
	echo -e 'Not a Mezzanine file:\n'$filename
	exit $?
fi
else
	echo -e 'This is not an mp4.\n'$filename'\n'
fi