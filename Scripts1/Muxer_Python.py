#!/usr/bin/python
import sys, os
import os
import os.path
import time
import datetime
import subprocess
import pipes

indir = '/Volumes/videos/videos/!muxer/'
outdir = '/Volumes/videos/videos/!muxer/Completed/'

fileName = os.path.basename(sys.argv[1])
filePath = os.path.dirname(sys.argv[1])
fileExtension = os.path.splitext(sys.argv[1])

#functions
def ffmpeg(sourceFile, audio, name360, name720, matchOut):
    print sourceFile
    print audio
    subprocess.Popen("ffmpeg -i %s -i %s -c:v copy -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [sourceFile, audio, matchOut])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
    subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [sourceFile, audio, name360])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
    length = subprocess.Popen(["ffprobe", sourceFile], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
    lStart = length.index("Duration: ") + 10
    lEnd = length.index(",", lStart)
    length = length[lStart:lEnd]
    now = datetime.datetime.now()
    t = datetime.datetime.strptime(length, "%H:%M:%S.%f")
    length = (60 * t.minute) + (60 * t.hour) + t.second
    bitRate = str((802816 / length) - 320) + "k"
    subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v %s -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [sourceFile, audio, bitRate, name720])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
    #shutil.copy(video360FileOut, deliveryFolder)
    #shutil.copy(video720FileOut, deliveryFolder)
    return

if fileName.endswith(".mp4"):
    audio = fileName[:-17] + "_MIX.wav"
    print filePath+'/'+audio
    if os.path.isfile(filePath+'/'+audio):
        audio = filePath+'/'+audio
        sourceFile = filePath+'/'+fileName
        name720 = outdir+fileName.replace('MATCH_SOURCE','720p')
        name360 = outdir+fileName.replace('MATCH_SOURCE','360p')
        matchOut = outdir+fileName.replace('MATCH_SOURCE', 'MATCH_SOURCE_MUXED')
        #print(name720)
        ffmpeg(sourceFile, audio, name360, name720, matchOut)
