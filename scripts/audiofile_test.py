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

podPath = '/Volumes/videos/pod_videos/' 
NoFolder = '/Volumes/audio_recordings/PODRecordings/VoiceOverCompleted/NoFolder'

fileName = os.path.basename(sys.argv[1])
filePath = os.path.dirname(sys.argv[1])
fileExtension = os.path.splitext(sys.argv[1])

projectName = fileName[:-11]

podFolder = podPath + projectName
print podFolder
audioFolder = podPath + projectName + '/01_assets/01_audio/01_VO/'
if os.path.isdir(podFolder): 
	print 'folder Found'
	print projectName
	#subprocess.Popen(['mv', sys.argv[1], audioFolder])
	if os.path.isfile(audioFolder + "/" + fileName):
		print "already copied"
		os.remove(audioFolder + "/" + fileName)
	shutil.move(sys.argv[1], audioFolder)
	recipient = 'alex.rivera@studiesweekly.com'
	subject = 'Audio Returned'
	body = projectName + ' audio has been recorded and processed to the correct folder on Jeeves.'
	def send_message(recipient, subject, body):
		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	send_message(recipient, subject, body)
	ResLine = worksheet.col_values(19)
	projectList = worksheet.col_values(6)
	lineNumber = projectList.index(projectName)
	EngVOLine = worksheet.col_values(19)
	projectList = worksheet.col_values(6)
	worksheet.update_cell((lineNumber + 1), 19, todaysDate)
else:
	print 'No folder found.'
	recipient = 'chris.smith@studiesweekly.com'
	subject = 'No audio folder'
	body = projectName + ' cant find the project folder on jeeves.'
	def send_message(recipient, subject, body):
		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	send_message(recipient, subject, body)
	subprocess.Popen(['mv', sys.argv[1], NoFolder])
