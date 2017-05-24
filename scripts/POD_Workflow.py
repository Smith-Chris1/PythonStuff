#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
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
global projectName
global projectCat
global folderName
global process
podPath = '/Volumes/pods/' 
relationPath = '/Volumes/related_media/'
folderStructure = '/Volumes/pods/_SupportingFiles'
audioFolder = '/Volumes/audio_recordings/PODRecordings/VoiceOverCompleted/'
ResearchFinished = '/Volumes/related_media/01_ResearchFinished/'
GoogleDrive = '/Users/transcoder/Desktop/POD_Workflow_Files/Google Drive/Folders'
CreativeTemplate = '/Users/transcoder/Desktop/POD_Workflow_Files/CreativeBrief_Template.docx'
EditTemplate = '/Users/transcoder/Desktop/POD_Workflow_Files/VideoEditingScriptTemplate.docx'
OMFLocation = '/Volumes/videos/Audio/ToAudio/'
MXFLocation = '/Volumes/videos/Audio/Proxy/'
now = datetime.datetime.now()
todaysDate = now.strftime("%m/%d/%Y")
scope = ['https://spreadsheets.google.com/feeds']
json_key = json.load(open('/Users/transcoder/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json'))
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/transcoder/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json', scope)
gc = gspread.authorize(credentials)

googleDoc = gc.open('Workflow Test')

worksheet = googleDoc.worksheet("Project Tracker")
#while True:

	#os.system('clear')
	#print 'Waiting for 1 minute.\n'
	#time.sleep(60)



#This section creates the Folder/Filename and folder structures on Jeeves.
print "Checking for updates with the Projects..."
FolderLine = worksheet.col_values(6)
projectWeek = worksheet.col_values(5)
projectCat = worksheet.col_values(2)
projectGrade = worksheet.col_values(3)
projectState = worksheet.col_values(4)
projectName = worksheet.col_values(1)
articleNumbers = worksheet.col_values(7)
del FolderLine[0]
ProjectlistNumber = 0
for x in FolderLine:
	if ProjectlistNumber < len(FolderLine) - 1:
		ProjectlistNumber = ProjectlistNumber + 1
		if x == '':
			if projectName[ProjectlistNumber] != '' and projectCat[ProjectlistNumber] != '' and projectGrade[ProjectlistNumber] != '' and projectState[ProjectlistNumber] != '' and projectWeek[ProjectlistNumber] != '':
				fixedName = projectName[ProjectlistNumber]
				fixedName = fixedName.replace(' ', '')
				fixedName = fixedName.replace('!', '')
				fixedName = fixedName.replace(',', '')
				fixedName = fixedName.replace('.', '')
				fixedName = fixedName.replace('?', '')
				fixedName = fixedName.replace('/', '')
				fixedName = fixedName.replace('&', '')
				fixedName = fixedName.replace('`', '')
				fixedName = fixedName.replace('"', '')
				fixedName = fixedName.replace(':', '')
				fixedName = fixedName.replace('(', '')
				fixedName = fixedName.replace(')', '')
				fixedName = fixedName.replace('-', '')
				fixedName = fixedName.replace("'", "")
				#fixedName = fixedName.replace("’", "")
				folderName = 'POD_' + projectGrade[ProjectlistNumber] + '_' + projectCat[ProjectlistNumber] + '_' + projectState[ProjectlistNumber] + '_' + fixedName + '_' + projectWeek[ProjectlistNumber]
				spanishName = 'POD_' + projectGrade[ProjectlistNumber] + '_' + projectCat[ProjectlistNumber] + '_' + projectState[ProjectlistNumber] + '_' + fixedName + '_' + projectWeek[ProjectlistNumber] + '_SPA'
				podPath1 = podPath + folderName
				projectPath = podPath + folderName + "/02_project/projectname_offline.prproj"
				NewProjectPath = podPath + folderName + "/02_project/" + folderName + ".prproj"
				relationPath1 = relationPath + folderName
				dirExists = os.path.exists(podPath1)
				print dirExists
				if dirExists == True:
					worksheet.update_cell((ProjectlistNumber + 1), 6, folderName + "!")
				else:
					print "Found new project " + fixedName + "Creating supporting folders."
					worksheet.update_cell((ProjectlistNumber + 1), 6, folderName)
					worksheet.update_cell((ProjectlistNumber + 1), 14, spanishName)
					os.makedirs(podPath1)
					distutils.dir_util.copy_tree(folderStructure, podPath1)
					os.rename(projectPath,NewProjectPath)
					#os.makedirs(relationPath1)
					os.makedirs(GoogleDrive + '/' + folderName)
					subprocess.Popen(['cp', CreativeTemplate, GoogleDrive + '/' + folderName + '/' + fixedName + '_creative_brief.docx'])
					subprocess.Popen(['cp', EditTemplate, GoogleDrive +'/' + folderName + '/' + fixedName + '_video_script.docx'])

#this will write the text file
print "Checking for a text file..."
FolderLine = worksheet.col_values(6)
projectWeek = worksheet.col_values(5)
projectCat = worksheet.col_values(2)
projectGrade = worksheet.col_values(3)
projectState = worksheet.col_values(4)
projectName = worksheet.col_values(1)
articleNumbers = worksheet.col_values(7)
ArticlelistNumber = 0
for x in articleNumbers:
	if ArticlelistNumber < len(articleNumbers) - 1:
		ArticlelistNumber = ArticlelistNumber + 1
		if x  != '':
			fixedName = FolderLine[ArticlelistNumber]
			#fixedName = fixedName.replace(' ', '')
			fixedName = fixedName.replace('!', '')
			#fixedName = fixedName.replace(',', '')
			#fixedName = fixedName.replace('.', '')
			#fixedName = fixedName.replace('?', '')
			#fixedName = fixedName.replace('/', '')
			#fixedName = fixedName.replace('&', '')
			#fixedName = fixedName.replace('`', '')
			#fixedName = fixedName.replace('"', '')
			#fixedName = fixedName.replace(':', '')
			#fixedName = fixedName.replace("'", "")
			#fixedName = fixedName.replace("’", "")
			#projectName1 = worksheet.cell(ArticlelistNumber, 6).value
			#folderName = 'POD_' + projectGrade[ArticlelistNumber] + '_' + projectCat[ArticlelistNumber] + '_' + projectState[ArticlelistNumber] + '_' + fixedName + '_' + projectWeek[ArticlelistNumber]
			textFile = GoogleDrive + '/' + fixedName + '/' + fixedName + '.txt'
			if articleNumbers[ArticlelistNumber] == '':
				file = True
			if os.path.isfile(textFile):
				file = True
			else:
				f = open(textFile, "w")
				f.write('https://www.studiesweekly.com/online/content/' + articleNumbers[ArticlelistNumber])
				f.close()

#This will email the script writer
print "Checking for updates with the Script Writer..."
ScriptLine = worksheet.col_values(9)
del ScriptLine[0]
ScriptlistNumber = 1
for x in ScriptLine:
	ScriptlistNumber = ScriptlistNumber + 1
	if x != '':
		if worksheet.cell(ScriptlistNumber, 10).value == '':
			import subprocess
			recipient = worksheet.cell(ScriptlistNumber, 9).value
			subject = 'New Script for POD Video'
			body = worksheet.cell(ScriptlistNumber, 8).value + ' Has assigned you a script to work on for ' + worksheet.cell(ScriptlistNumber, 6).value
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
  			send_message(recipient, subject, body)
			worksheet.update_cell(ScriptlistNumber, 10, todaysDate)

#This will email the english VO talent
print "Checking for updates with the English VO Talent..."
EngVOLine = worksheet.col_values(12)
del EngVOLine[0]
EngVOlistNumber = 1
for x in EngVOLine:
	EngVOlistNumber = EngVOlistNumber + 1
	if x != '':
		if worksheet.cell(EngVOlistNumber, 13).value == '':
			import subprocess
			recipient = worksheet.cell(EngVOlistNumber, 12).value
			if recipient == "danor.gerald@imminentcatharsis.com":
				recipient = "chris.smith@studiesweekly.com"
			subject = 'New Script for POD Video'
			body = worksheet.cell(EngVOlistNumber, 8).value + ' Has assigned you a Voice Over for ' + worksheet.cell(EngVOlistNumber, 6).value + ' Please name the file you send back to us: ' + worksheet.cell(EngVOlistNumber, 6).value + '_ENG_VO.wav' + " And place it in this folder: " + audioFolder
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
  			send_message(recipient, subject, body)
			worksheet.update_cell(EngVOlistNumber, 13, todaysDate)

#This will email the spanish VO talent
print "Checking for updates with the Spanish VO Talent..."
SpaVOLine = worksheet.col_values(17)
del SpaVOLine[0]
SpaVOlistNumber = 1
for x in SpaVOLine:
	SpaVOlistNumber = SpaVOlistNumber + 1
	if x != '':
		if worksheet.cell(SpaVOlistNumber, 18).value == '':
			import subprocess
			recipient = worksheet.cell(SpaVOlistNumber, 17).value
			subject = 'New Script for POD Video'
			body = worksheet.cell(SpaVOlistNumber, 8).value + ' Has assigned you a Voice Over for ' + worksheet.cell(SpaVOlistNumber, 6).value + ' Please name the file you send back to us: ' + worksheet.cell(SpaVOlistNumber, 6).value + '_SPA_VO.wav' + " And place it in this folder: " + audioFolder
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
  			send_message(recipient, subject, body)
			worksheet.update_cell(SpaVOlistNumber, 18, todaysDate)

#This will email the researcher
print "Checking for updates with the Researcher..."
ResLine = worksheet.col_values(21)
del ResLine[0]
ReslistNumber = 1
for x in ResLine:
	ReslistNumber = ReslistNumber + 1
	if x != '':
		if worksheet.cell(ReslistNumber, 22).value == '':
			import subprocess
			recipient = worksheet.cell(ReslistNumber, 21).value
			subject = 'New Script for POD Video'
			body = worksheet.cell(ReslistNumber, 8).value + ' Has assigned you to research ' + worksheet.cell(ReslistNumber, 6).value + ' Please place your folder here when research is complete: ' + ResearchFinished
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
 			send_message(recipient, subject, body)
			worksheet.update_cell(ReslistNumber, 22, todaysDate)

#This will email the editor
print "Checking for updates with the Editor..."
EditLine = worksheet.col_values(24)
del EditLine[0]
EditlistNumber = 1
for x in EditLine:
	EditlistNumber = EditlistNumber + 1
	if x != '':
		if worksheet.cell(EditlistNumber, 25).value == '':
			import subprocess
			recipient = worksheet.cell(EditlistNumber, 24).value
			subject = 'New Edit for POD Video'
			body = worksheet.cell(EditlistNumber, 8).value + ' Has assigned you to edit ' + worksheet.cell(EditlistNumber, 6).value
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
  			send_message(recipient, subject, body)
			worksheet.update_cell(EditlistNumber, 25, todaysDate)

#This will email the spanish translator
print "Checking for updates with the Spanish Translator..."
EditLine = worksheet.col_values(15)
del EditLine[0]
EditlistNumber = 1
for x in EditLine:
	EditlistNumber = EditlistNumber + 1
	if x != '':
		if worksheet.cell(EditlistNumber, 16).value == '':
			import subprocess
			recipient = worksheet.cell(EditlistNumber, 15).value
			subject = 'New Translation for POD Video'
			body = worksheet.cell(EditlistNumber, 8).value + ' Has assigned you to translate ' + worksheet.cell(EditlistNumber, 6).value
			def send_message(recipient, subject, body):
				subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
  			send_message(recipient, subject, body)
			worksheet.update_cell(EditlistNumber, 16, todaysDate)

