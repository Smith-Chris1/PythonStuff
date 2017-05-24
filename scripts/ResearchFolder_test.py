#!/usr/bin/python
import sys, os
import time
import subprocess
import gspread
import json
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
NoFolder = '/Volumes/related_media/01_ResearchFinished/noFolder'

folderName = os.path.basename(sys.argv[1])
folderPath = os.path.dirname(sys.argv[1])

projectName = folderName
files = os.listdir(sys.argv[1])

podFolder = podPath + projectName
print podFolder

imageFolder = podPath + projectName + '/01_assets/02_graphics/01_pictures/'
if os.path.isdir(podFolder): 
	print 'folder Found'
	print projectName
	for file in files:
		print file
		#subprocess.Popen(['mv', sys.argv[1] + "/" + file, imageFolder])
		#time.sleep(30)
		if not file.startswith('.'):
			if os.path.isfile(imageFolder + "/" + file):
				print "already copied"
				os.remove(imageFolder + "/" + file)
			shutil.move(sys.argv[1] + "/" + file, imageFolder)
	#recipient = 'alex.rivera@studiesweekly.com'
	#subject = 'Research Returned'
	#body = projectName + ' images and video have been processed to the correct folder on Jeeves.'
	#def send_message(recipient, subject, body):
	#	subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	#send_message(recipient, subject, body)
	ResLine = worksheet.col_values(23)
	projectList = worksheet.col_values(6)
	lineNumber = projectList.index(projectName)
	worksheet.update_cell((lineNumber + 1), 23, todaysDate)
	os.rmdir(sys.argv[1])
else:
	print 'No folder found.'
	recipient = 'chris.smith@studiesweekly.com'
	subject = 'No research folder'
	body = projectName + ' cant find the project folder on jeeves.'
	def send_message(recipient, subject, body):
		subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
	send_message(recipient, subject, body)
	subprocess.Popen(['mv', sys.argv[1], NoFolder])
