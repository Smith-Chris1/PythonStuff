import shutil
import sys, os
import os.path
import subprocess
import pipes

file = os.path.basename(sys.argv[1])
fileName = os.path.splitext(file)[0]
filePath = os.path.dirname(sys.argv[1])
fileExtension = os.path.splitext(file)[1]
fileDestination = "/Volumes/audio_recordings/ArticleRecordings/All Audio Files/"

def ffmpegEncode(fileName, fileDestination):
	subprocess.Popen("ffmpeg -i %s -vn -c:a libmp3lame -b:a 320k %s %s" % tuple(map(pipes.quote, sys.argv[1], audioFilters, fileDestination)),stdout=subprocess.PIPE,shell=True).communicate()[0]
	return

def ffmpegLUFS(fileName):
	print "the file is: " + fileName
	#subprocess.Popen("ffmpeg -i %s -filter_complex ebur128 -f null - 2>&1 | grep -n '.*' | grep -A 5 'size' | grep 'I:' | cut -d ':' -f3-" % pipes.quote(fileName))
	length = subprocess.Popen(["/usr/local/Cellar/ffmpeg/3.0/bin/ffprobe", fileName], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
	lStart = length.index("size") + 10
	#subprocess.call(['ffmpeg', '-i', fileName, '-filter_complex', 'ebur128', '-f', 'null', "'- 2>&1 |'" "'grep -n '.*' | grep -A 5 'size' | grep 'I:' | cut -d ':' -f3-'"], stdout=subprocess.PIPE)
	return

print fileName
print fileExtension
mainFolder = fileName.rsplit("_")[0]
week = fileName.rsplit("_")[1]
weekFolder = week.rsplit("#")[0]
ID = fileName.rsplit("#")[2]
print "Main folder = " + mainFolder
print "Week folder = " + weekFolder
print "ID = " + ID
sourceLUFS = ffmpegLUFS(sys.argv[1])
print "The source loudness is: " + sourceLUFS
HeatherAudioFilters = "-filter_complex equalizer=f=112:width_type=h:width=200:g=18,equalizer=f=164:width_type=h:width=200:g=-5,equalizer=f=393:width_type=h:width=200:g=-3.4,equalizer=f=2540:width_type=h:width=200:g=-3.4,equalizer=f=8520:width_type=h:width=200:g=.7"
AJAudioFilters = "-filter_complex equalizer=f=99:width_type=h:width=200:g=18,equalizer=f=148.5:width_type=h:width=200:g=-3.8,equalizer=f=433.7:width_type=h:width=200:g=-7.3,equalizer=f=2120:width_type=h:width=200:g=-5.2,equalizer=f=10810:width_type=h:width=200:g=2.6"
DaveyAudioFilters = "-filter_complex equalizer=f=97:width_type=h:width=200:g=18,equalizer=f=137:width_type=h:width=200:g=-4.8,equalizer=f=460.4:width_type=h:width=200:g=-4.8,equalizer=f=2040:width_type=h:width=200:g=-4.6,equalizer=f=8190:width_type=h:width=200:g=1.7"
SoraidaAudioFilters = "-filter_complex equalizer=f=98:width_type=h:width=200:g=18,equalizer=f=208:width_type=h:width=200:g=.5,equalizer=f=1710:width_type=h:width=200:g=-6.3,equalizer=f=6450:width_type=h:width=200:g=-5.4,equalizer=f=13180:width_type=h:width=200:g=-5.7"
EmmaAudioFilters = "-filter_complex equalizer=f=112:width_type=h:width=200:g=18,equalizer=f=216:width_type=h:width=200:g=-2.8,equalizer=f=835:width_type=h:width=200:g=-3,equalizer=f=3350:width_type=h:width=200:g=-2.6,equalizer=f=13990:width_type=h:width=200:g=2.8"
fileDestination = os.path.dirname(sys.argv[1])
#ffmpegEncode(file, audioFilters, "/Volumes/audio_recordings/Workflow_Test/test.mp3")


#!/bin/bash
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"

	then
	clear
	echo -e 'Currently processing:\n'$filename'\nEncoding will begin shortly.\n'
	#sleep 60
	newName=${filename/_Temp/_360p}
	ffmpeg -y -i "$directory/$filename.mp4" -i $2 -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a "$directory"/"$newName".mp4
	newName=${filename/_Temp/_720p}
	sourceLUFS=$(ffmpeg -i "$directory/$filename.mp4" 2>&1 | grep -n '.*' | grep -A 5 'size' | grep 'I:' | cut -d ':' -f3-)
	echo $sourceLUFS

	#echo $bitRaten
	#ffmpeg -y -i "$directory/$filename.mp4" -i $2 -c:v libx264 -b:v $bitRate -preset veryslow -level 4.0 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a "$directory"/"$newName".mp4
