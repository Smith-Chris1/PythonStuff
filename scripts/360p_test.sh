filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
bitRate=5000k
editor=chris.smith@studiesweekly.com
directory="/Volumes/videos/!export_temp/360p"
completed="/Volumes/videos/!export_temp/Completed"
time=$((5*60))
CUR=$time
newName=${filename/_720p/_360p}
	if [[ $filename == *"SPA"* ]]
		then
		moveTo="/Volumes/videos/!720p/!SPA"
	else
		moveTo="/Volumes/videos/!720p/!ENG"
	fi
ffmpeg -y -i $1 -pix_fmt yuv420p -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k "$moveTo"/"$newName".mp4
	#mv "$directory"/"$newName".mp4 $moveTo
mv $1 $completed
#newName=${filename/_MATCH_SOURCE/_720p}
#length=$(ffmpeg -i "$directory/$filename.$extension" 2>&1 | grep "Duration" | cut -d ' ' -f 4 | sed s/,// | sed 's@\..*@@g' | awk '{ split($1, A, ":"); split(A[3], B, "."); #print 3600*A[1] + 60*A[2] + B[1] }')
#	bitRate=$(( (802816 / $length) - 320))k
#ffmpeg -y -i "$directory/$filename.$extension" -pix_fmt yuv420p -c:v libx264 -b:v $bitRate -preset veryslow -profile:v high -level 4.0 -vf unsharp -vf scale=1280:720 -strict #-2 -c:a libfdk_aac -b:a 320k "$directory"/"$newName".mp4
#	cp "$directory"/"$newName".mp4 $moveTo
#	mv "$directory"/"$newName".mp4 $completed
#mail -s "transcode complete: $newName.mp4" $editor <<< "The file: $newName.mp4 can be found here: $completed
#mail -s "File ready for upload: $newName.mp4" #megan.denbow@studiesweekly.com <<< "This file: $newName.mp4 can be #found here: $moveTo Please check for quality and upload."	