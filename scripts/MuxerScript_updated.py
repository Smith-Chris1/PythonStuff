#!/usr/bin/python
import sys, os
import time
import subprocess
import gspread
import json
import os
import os.path
import distutils.core
import datetime
import numpy as np
import shutil
import pipes
from subprocess import check_call
from email.mime.text import MIMEText
from oauth2client.service_account import ServiceAccountCredentials
now = datetime.datetime.now()
todaysDate = now.strftime("%m/%d/%Y")
scope = ['https://spreadsheets.google.com/feeds']
json_key = json.load(open('/Users/transcoder/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json'))
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/transcoder/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json', scope)
gc = gspread.authorize(credentials)

googleDoc = gc.open('Workflow Test')

worksheet = googleDoc.worksheet("Project Tracker")

podPath = '/Volumes/pods/' 
NoFolder = '/Volumes/pods/FromAudio/noFolder'

fileName = os.path.basename(sys.argv[1])
filePath = os.path.dirname(sys.argv[1])
fileExtension = os.path.splitext(sys.argv[1])

PODLocation = "/Volumes/pods/!Future_Videos"
FromEditors = "/Volumes/pods/FromEditors"
FromAudio = "/Volumes/pods/FromAudio/"
NotProcessed = "/Volumes/pods/FromAudio/NotProcessed"
OmfFolder = "/Volumes/pods/FromEditors/01_temp_OMF"
FTPFolder = "/to_be_mixed/"
CompleteFolder = "/Volumes/pods/!COMPLETED"
renameFolder = "/Volumes/pods/FromEditors/01_temp_OMF/rename"
now = datetime.datetime.now()
todaysDate = now.strftime("%m%d%Y")
success = False
#deliveryFolder = "/Volumes/videos/videos/!720p/!ENG"
ToDelete = "/Volumes/pods/FromEditors/TEMP"

#functions
def ffmpeg(fixedName, fileDestination, language):
	videoFileIn = fileDestination + "/" + fixedName + "_" + language + "_temp.mp4"
	print videoFileIn
	if os.path.isfile(videoFileIn):
		print "Found video file"
	videoMatchSourceFileOut = fileDestination + "/" + fixedName + "_" + language + "_" + todaysDate + "_MATCH_SOURCE.mp4"
	video360FileOut = fileDestination + "/" + fixedName + "_" + language + "_" + todaysDate + "_360p.mp4"
	video720FileOut = fileDestination + "/" + fixedName + "_" + language + "_" + todaysDate + "_720p.mp4"
	subprocess.Popen("/usr/local/Cellar/ffmpeg/3.0/bin/ffmpeg -i %s -i %s -c:v copy -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, sys.argv[1], videoMatchSourceFileOut])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
	subprocess.Popen("/usr/local/Cellar/ffmpeg/3.0/bin/ffmpeg -i %s -i %s -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, sys.argv[1], video360FileOut])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
	length = subprocess.Popen(["/usr/local/Cellar/ffmpeg/3.0/bin/ffprobe", videoFileIn], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
	lStart = length.index("Duration: ") + 10
	lEnd = length.index(",", lStart)
	length = length[lStart:lEnd]
	t = datetime.datetime.strptime(length, "%H:%M:%S.%f")
	length = (60 * t.minute) + (60 * t.hour) + t.second
	bitRate = str((802816 / length) - 320) + "k"
	subprocess.Popen("/usr/local/Cellar/ffmpeg/3.0/bin/ffmpeg -i %s -i %s -c:v libx264 -b:v %s -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, sys.argv[1], bitRate, video720FileOut])),stdout=subprocess.PIPE,
						shell=True).communicate()[0]
	shutil.copy(video360FileOut, deliveryFolder)
	shutil.copy(video720FileOut, deliveryFolder)
	return


print "I'm working on " + (sys.argv[1])
category = fileName.rsplit("_")[0]  
grade = fileName.rsplit("_")[1]
catType = fileName.rsplit("_")[2]
state = fileName.rsplit("_")[3] 
projectName = fileName.rsplit("_")[4] 
pubWeek = fileName.rsplit("_")[5]
language = fileName.rsplit("_")[6] 
fixedName = category + "_" + grade + "_" + catType + "_" + state + "_" + projectName + "_" + pubWeek
deliveryFolder = "/Volumes/videos/videos/!720p/!" + language

#fixedName = item.replace('_MIX.wav', '')
FoldStruct1 = FromEditors + "/" + fixedName + "/03_Final"
FoldStruct2 = FromEditors + "/" + fixedName + "/assets/OMF"
FoldStruct3 = FromEditors + "/" + fixedName + "/assets/OMF"

#Add OMF and _Temp MP4s sorting here
print fixedName

if os.path.isdir(FoldStruct1) | os.path.isdir(FoldStruct2): 
	print 'folder Found'
	print projectName
	print fixedName
	if os.path.isdir(FoldStruct1) == True:
		fileDestination = FoldStruct1
		audioCopy = FromEditors + "/" + fixedName + "/01_assets/01_audio/05_final_mix"
		print "Found Folder Structure 1"
	if os.path.isdir(FoldStruct2) == True:
		fileDestination = FoldStruct2
		audioCopy = FromEditors + "/" + fixedName + "/assets/audio"
		print "Found Folder Structure 2"
	ffmpeg(fixedName, fileDestination, language)
	shutil.move(sys.argv[1], audioCopy)
	FoldCopy1 = FromEditors + "/" + fixedName
	PODCopy = PODLocation + "/" + fixedName
	check_call("rsync -aP %s/* %s" % tuple(map(pipes.quote, [FoldCopy1, PODCopy])),
							shell=True)
	subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [FoldCopy1, ToDelete])),
							shell=True)

	#if os.path.isfile(FoldStruct1 + "/" + fileName):
	#	print "already copied"
	#	os.remove(audioFolder + "/" + fileName)
	#shutil.move(sys.argv[1], audioFolder)
	#recipient = 'alex.rivera@studiesweekly.com'
	#subject = 'Audio Returned'
	#body = projectName + ' audio has been recorded and processed to the correct folder on Jeeves.'
	#def send_message(recipient, subject, body):
	#	subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	#send_message(recipient, subject, body)
	#ResLine = worksheet.col_values(19)
	#projectList = worksheet.col_values(6)
	#lineNumber = projectList.index(projectName)
	#EngVOLine = worksheet.col_values(19)
	#projectList = worksheet.col_values(6)
	#worksheet.update_cell((lineNumber + 1), 19, todaysDate)
else:
	print 'No folder found.'
	recipient = 'chris.smith@studiesweekly.com'
	subject = 'No audio folder'
	body = projectName + ' cant find the project folder on jeeves.'
	def send_message(recipient, subject, body):
		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	send_message(recipient, subject, body)
	shutil.move(sys.argv[1], NoFolder)
