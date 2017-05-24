#!/bin/bash
input=(/Users/chrissmith/Desktop/POD_VIDEOS_AWS/*)
#folder="Users/chrissmith/Desktop/POD_VIDEOS_AWS"

for f in "${input[@]}"
 do
    filename=$(basename "$f")
    folder="${filename%.*}"
    length=$(ffmpeg -i "$f" 2>&1 | grep "Duration" | cut -d ' ' -f 4 | sed s/,// | sed 's@\..*@@g' | awk '{ split($1, A, ":"); split(A[3], B, "."); print 3600*A[1] + 60*A[2] + B[1] }')
    #echo $filename "," $length
    echo $filename "," $length >> /Users/chrissmith/Desktop/AWSLength.txt
    #echo " , " >> /Users/chrissmith/Desktop/AWSLength.txt

 done