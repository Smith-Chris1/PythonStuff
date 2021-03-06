/Users/chrissmith/Desktop/watchfile.sh -s "find /Volumes/videos/\!export_temp -type f -print0 | xargs -0 stat" -e echo $f
#output="/Volumes/videos/!export_temp"
#filename=$(basename "$1")
#directory=$(dirname "$1")
#extension="${filename##*.}"
#filename="${filename%.*}"
#if [[ $extension == "mp4" ]]
#echo $directory
#echo $filename
#echo $extension
#then
#if [[ $filename == *"_MATCH_SOURCE"* ]]
#	then
#	clear
#	echo -e 'Currently processing:\n'$filename'\nEncoding will begin shortly.\n'
#	sleep 60
#	newName=${filename/_MATCH_SOURCE/_360p}
#	ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -pass 1 -strict -2 -c:a copy -f mp4 /dev/null && \ 
#	ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -pass 2 -strict -2 -c:a copy "$output"/"$newName".mp4
#	newName=${filename/_MATCH_SOURCE/_720p}
#	length=$(ffmpeg -i "$directory/$filename.mp4" 2>&1 | grep "Duration" | cut -d ' ' -f 4 | sed s/,// | sed 's@\..*@@g' | awk '{ split($1, A, ":"); split(A[3], B, "."); print 3600*A[1] + 60*A[2] + B[1] }')
#	#echo $length
#	bitRate=$(( (802816 / $length) - 320))k
#	#echo $bitRate
#	#ffmpeg -i "$1" -c:v libx264 -b:v 9m -preset veryslow -profile:v high -level 4.0 -vf unsharp -vf scale=1280:720 -strict -2 -c:a copy "$output"/"$newName"."$extension" #This is a Single Pass
#	ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v $bitRate -preset veryslow -profile:v high -level 4.0 -vf unsharp -vf scale=1280:720 -pass 1 -strict -2 -c:a copy -f mp4 /dev/null && \ 
#	ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v $bitRate -preset veryslow -profile:v high -level 4.0 -vf unsharp -vf scale=1280:720 -pass 2 -strict -2 -c:a copy "$output"/"$newName".mp4
#else
#	echo -e 'Not a Mezzanine file:\n'$filename
#	exit $?
#fi
#else
#	echo -e 'This is not an mp4.\n'$filename'\n'
#fi