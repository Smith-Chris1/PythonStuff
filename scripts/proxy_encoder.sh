filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
newName=${filename/_Temp/_Audio}
baseName=${filename/_Temp/ }
ffmpeg -y -i "$directory/$filename.mp4" -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a copy "$directory"/"$newName".mp4
mv $1 /volumes/