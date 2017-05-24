#!/usr/bin/python
import os
import shutil
import os.path
import pipes
import datetime
import re
import fnmatch
from subprocess import check_call
import subprocess
import ftplib
import sys
import time
PODLocation = "/Volumes/pods/!Future_Videos"
FromEditors = "/Volumes/pods/FromEditors"
FromAudio = "/Volumes/pods/FromAudio/"
NotProcessed = "/Volumes/pods/FromAudio/NotProcessed"
uploadFolder = "/Volumes/videos/!mix_temp"
FTPFolder = "/to_be_mixed/"
CompleteFolder = "/Volumes/pods/!COMPLETED"
renameFolder = "/Volumes/pods/FromEditors/01_temp_OMF/rename"
now = datetime.datetime.now()
todaysDate = now.strftime("%m%d%Y")
success = False
deliveryFolder = "/Volumes/videos/!720p/!ENG"
ToDelete = "/Volumes/pods//FromEditors/TEMP"
OmfFolder = "/Volumes/videos/!mix_temp/Uploaded"

#functions
def uploadFTP(uploadFile):
	session = ftplib.FTP('ftp.blufirestudios.com','studiestransfer@blufirestudios.com','audiosw33t')
	filename, file_extension = os.path.splitext(uploadFile)
	filename = os.path.basename(uploadFile)
	#print filename
	file1 = open(uploadFile, 'rb')
	session.cwd(FTPFolder)
	#print file1
	session.storbinary('STOR ' + filename, file1)
	return

#Upload OMF and MP4 to Audio
filename, file_extension = os.path.splitext(sys.argv[1])
file = sys.argv[1]
print "I'm working on " + filename
category = filename.rsplit("_")[0]  
grade = filename.rsplit("_")[1]
catType = filename.rsplit("_")[2]
state = filename.rsplit("_")[3] 
projectName = filename.rsplit("_")[4] 
pubWeek = filename.rsplit("_")[5]
language = filename.rsplit("_")[6] 
fixedName = category + "_" + grade + "_" + catType + "_" + state + "_" + projectName + "_" + pubWeek
#MP4filename = FromEditors + "/01_temp_OMF/" + fixedName + "_" + language + "_Temp.mp4"
if file_extension == '.txt':
	textFile = os.path.join(uploadFolder, sys.argv[1])
	os.remove(textFile)
if file_extension == '.omf':
	OMFfilename = os.path.join(uploadFolder, sys.argv[1])
	print "Found OMF:" + file
	uploadFTP(sys.argv[1])
	recipient = 'chris.smith@studiesweekly.com,alex.rivera@studiesweekly.com'
	subject = 'File Uploaded to BluFire FTP'
	body = 'Nate, I have uploaded a file: ' + filename + ' to your ftp. Please name the final wav you deliver ' + fixedName + language + "_Mix.wav. Let me know if you have any issues or questions."
	subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	shutil.move(sys.argv[1], OmfFolder)
if file_extension == '.mp4':
	MP4filename = os.path.basename(sys.argv[1])
	MP4filename = MP4filename[:-8]
	print MP4filename
	VideoAudioFileOut = OmfFolder + "/" + MP4filename + "temp.mp4"
	subprocess.Popen('/usr/local/Cellar/ffmpeg/3.0/bin/ffmpeg -y -i %s -c:v libx264 -b:v 1500k -preset fast -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a copy %s' % tuple(map(pipes.quote, [sys.argv[1], VideoAudioFileOut])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
	uploadFTP(VideoAudioFileOut)
	os.remove(VideoAudioFileOut)
	shutil.move(sys.argv[1], OmfFolder)

