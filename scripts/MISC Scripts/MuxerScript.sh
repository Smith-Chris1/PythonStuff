#!/bin/bash
PODLocation="/Volumes/videos/pod_videos/!Future_Videos/"
FromEditors="/Volumes/videos/pod_videos/FromEditors/"
FromAudio="/Volumes/videos/pod_videos/FromAudio/*.wav"

for f in $FromAudio 
	do
	filename=$(basename "$f")
	directory=$(dirname "$f")
	extension="${filename##*.}"
	filename="${filename%.*}"
	#echo $f
	$FolderName=${filename/_MIX.wav/" "}
	FoldStruct1=$FromEditors "/" $filename "/03_Final"
	#FoldStruct2=
	#FoldStruct3=
	if [ -d FoldStruct1 ]; then
		echo "I see the folder! " FoldStruct1
	fi
done 





