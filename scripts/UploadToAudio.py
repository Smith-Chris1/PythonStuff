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

podPath = '/Volumes/videos/pod_videos/FromEditors/' 
NoFolder = '/Volumes/videos/pod_videos/FromEditors/01_temp_OMF/NoFolder'

fileName = os.path.basename(sys.argv[1])
filePath = os.path.dirname(sys.argv[1])

projectName = fileName[:-13]

podFolder = podPath + projectName + '_ENG'

FinalFolder1 = podFolder + '/03_Final'
FinalFolder2 = podFolder + '/final'
if os.path.isdir(podFolder): 
	print 'folder Found'
	print projectName
	first = subprocess.Popen(['/bin/echo', sys.argv[1]], stdout=subprocess.PIPE)
	second = subprocess.Popen(['bash', '/Users/transcoder/Desktop/POD_Workflow_Files/proxy_encoder.sh', sys.argv[1]], stdin=first.stdout)
#	if os.path.isdir(FinalFolder1):
#		shutil.move(sys.argv[1] , FinalFolder1)
#	if os.path.isdir(FinalFolder2):
#		shutil.move(sys.argv[1] , FinalFolder2)
#	subprocess.Popen(['mv', sys.argv[1], audioFolder])
#	recipient = 'alex.rivera@studiesweekly.com'
#	subject = 'Audio Returned'
#	body = projectName + ' audio has been recorded and processed to the correct folder on Jeeves.'
#	def send_message(recipient, subject, body):
#		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
#	send_message(recipient, subject, body)
#	EngVOLine = worksheet.col_values(17)
#	projectList = worksheet.col_values(6)
#	lineNumber = projectList.index(projectName)
#	worksheet.update_cell((lineNumber + 1), 17, todaysDate)
#else:
#	print 'No folder found.'
#	recipient = 'chris.smith@studiesweekly.com'
#	subject = 'No audio folder'
#	body = projectName + ' cant find the project folder on jeeves.'
#	def send_message(recipient, subject, body):
#		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
#	send_message(recipient, subject, body)
#	subprocess.Popen(['mv', sys.argv[1], NoFolder])
#