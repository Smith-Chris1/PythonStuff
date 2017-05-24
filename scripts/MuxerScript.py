#!/usr/bin/python
import os
import shutil
import os.path
import pipes
import datetime
import re
from subprocess import check_call
import subprocess
from ftplib import FTP
PODLocation = "/Volumes/pods/!Future_Videos"
FromEditors = "/Volumes/pods/FromEditors"
FromAudio = "/Volumes/pods/FromAudio/"
NotProcessed = "/Volumes/pods/FromAudio/NotProcessed"
OmfFolder = "/Volumes/pods/FromEditors/01_temp_OMF"
FTPFolder = "/to_be_mixed/"
CompleteFolder = "/Volumes/pods/!COMPLETED"
now = datetime.datetime.now()
todaysDate = now.strftime("%m%d%Y")
success = False
deliveryFolder = "/Volumes/videos/videos/!720p/!ENG"
ToDelete = "/Volumes/pods/FromEditors/TEMP"

#Upload OMF and MP4 to Audio
for (item) in os.listdir(OmfFolder):
	if not item.startswith('.') and os.path.isfile(os.path.join(OmfFolder, item)):
		fixedName = item.replace('_temp.mp4', '')
		fixedName = item.replace('_Temp.mp4', '')
		fixedName = item.replace('.omf', '')
		filename, file_extension = os.path.splitext(item)
		foldname = filename.replace("_Temp", '')
		foldname = filename.replace('_temp', '')
		OmfStruct1 = FromEditors + "/" + foldname + "/01_assets/01_audio/04_OMF"
		OmfStruct2 = FromEditors + "/" + foldname + "/assets/OMF"
		OmfStruct3 = FromEditors + "/" + foldname + "/03_final"
		Mp4Struct1 = FromEditors + "/" + foldname + "/03_Final"
		Mp4Struct2 = FromEditors + "/" + foldname + "/final"
		Mp4Struct3 = FromEditors + "/" + foldname + "/03_final"
		dirExists1 = os.path.isdir(OmfStruct1)
		dirExists2 = os.path.isdir(OmfStruct2)
		dirExists3 = os.path.isdir(OmfStruct3)
		#MP4filename = FromEditors + "/01_temp_OMF/" + foldname + "_Temp.mp4"
		if file_extension == '.txt':
			textFile = os.path.join(OmfFolder, item)
			os.remove(textFile)
		if file_extension == '.omf':
			MP4filename = FromEditors + "/01_temp_OMF/" + foldname + "_Temp.mp4"
			OMFfilename = os.path.join(OmfFolder, item)
			Mp4UploadName = foldname + "_Temp.mp4"
			ftp = FTP("ftp.blufirestudios.com")
			ftp.login("studiestransfer@blufirestudios.com", "audiosw33t")
			ftp.cwd(FTPFolder)
			file = open(OMFfilename, "rb")
			file1 = open(MP4filename, "rb") 
			ftp.storbinary('STOR ' + Mp4UploadName, file1) 
			ftp.storbinary('STOR ' + item, file)
			#ftp.quit()
			#file.close()
			recipient = 'chris.smith@studiesweekly.com,alex.rivera@studiesweekly.com'
			subject = 'File Uploaded to BluFire FTP'
			body = 'Nate, I have uploaded a file: ' + item + ' to your ftp. Please name the final wav you deliver ' + foldname + "_Mix.wav. Let me know if you have any issues or questions."
			subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
			if dirExists1 == True:
				print "Using Dir 1"
				subprocess.Popen(['mv', MP4filename, Mp4Struct1])
				subprocess.Popen(['mv', OMFfilename, OmfStruct1])
				print "file copied"
			if dirExists2 == True:
				print "Using Dir 2"
				subprocess.Popen(['mv', MP4filename, Mp4Struct2])
				subprocess.Popen(['mv', OMFfilename, OmfStruct2])
				print "file copied"
		
		
for (item) in os.listdir(FromAudio):
		if not item.startswith('.'): 
				fixedName = item.replace('_MIX.wav', '')
				FoldStruct1 = FromEditors + "/" + fixedName + "/03_Final"
				FoldStruct2 = FromEditors + "/" + fixedName + "/assets/OMF"
				FoldStruct3 = FromEditors + "/" + fixedName + "/assets/OMF"
				dirExists1 = os.path.isdir(FoldStruct1)
				dirExists2 = os.path.isdir(FoldStruct2)
#Add OMF and _Temp MP4s sorting here



#New Folder Structure
				if dirExists1 == True: 
					FoldCopy1 = FromEditors + "/" + fixedName
					PODCopy = PODLocation + "/" + fixedName
					AUDLocation = PODCopy + "/01_assets/01_audio/05_Final_mix/"
					audioFile = FromAudio + item
					ffAudioFile = PODCopy + "/01_assets/01_audio/05_Final_mix/" + item
					check_call("rsync -aP %s/* %s" % tuple(map(pipes.quote, [FoldCopy1, PODCopy])),
											shell=True)
					print audioFile
					print PODLocation
					print FoldCopy1
					print PODLocation
					print AUDLocation
					print audioFile
					print "These files: " + FoldCopy1 + " have been copied to: " + AUDLocation
					print "Deleting old files: "
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [audioFile, AUDLocation])),
									shell=True)
					#subprocess.Popen(['rmdir', fname ])
					#ffmpeg MATCH_SOURCE
					videoFileIn = "/Volumes/pods/!Future_Videos/" + fixedName + "/03_Final/" + fixedName + "_Temp.mp4"
					videoMatchSourceFileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/03_Final/" + fixedName + "_" + todaysDate + "_MATCH_SOURCE.mp4"
					video360FileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/03_Final/" + fixedName + "_" + todaysDate + "_360p.mp4"
					video720FileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/03_Final/" + fixedName + "_" + todaysDate + "_720p.mp4"
					subprocess.Popen("ffmpeg -i %s -i %s -c:v copy -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, audioFile, videoMatchSourceFileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					#ffmpeg 360
					subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, ffAudioFile, video360FileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					#ffmpeg 720 bitrate
					length = subprocess.Popen(["ffprobe", videoFileIn], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
					lStart = length.index("Duration: ") + 10
					lEnd = length.index(",", lStart)
					length = length[lStart:lEnd]
					t = datetime.datetime.strptime(length, "%H:%M:%S.%f")
					length = (60 * t.minute) + (60 * t.hour) + t.second
					bitRate = str((802816 / length) - 320) + "k"
					#ffmpeg 720
					subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v %s -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, ffAudioFile, bitRate, video720FileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					subprocess.Popen("cp %s %s" % tuple(map(pipes.quote, [video360FileOut, deliveryFolder])),
									shell=True)
					subprocess.Popen("cp %s %s" % tuple(map(pipes.quote, [video720FileOut, deliveryFolder])),
									shell=True)
					recipient = 'megan.denbow@studiesweekly.com,alex.rivera@studiesweekly.com'
					subject = 'POD Video Complete'
					body = 'A new POD video has been completed: ' + video360FileOut + ' ' + video720FileOut + ' You can find them in the !720p folder. Please QC and upload. Let Loki and Chris know if there are any issues.'
					subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [FoldCopy1, ToDelete])),
											shell=True)
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [PODCopy, CompleteFolder])),
											shell=True)


#Old FolderStructure
				if dirExists2 == True: 
					fixedName = item.replace('_MIX.wav', '')
					FoldCopy2 = FromEditors + "/" + fixedName
					PODCopy = PODLocation + "/" + fixedName
					AUDLocation = PODCopy + "/assets/final_mix/"
					audioFile = FromAudio + item
					ffAudioFile = PODCopy + "/assets/final_mix/" + item
					check_call("rsync -aP %s/* %s" % tuple(map(pipes.quote, [FoldCopy2, PODCopy])),
											shell=True)
					print audioFile
					print PODLocation
					print FoldCopy2
					print PODLocation
					print AUDLocation
					print audioFile
					print "These files: " + FoldStruct1 + " have been copied to: " + AUDLocation
					print "Deleting old files: "
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [audioFile, AUDLocation])),
									shell=True)
					#subprocess.Popen(['rmdir', fname ])
					#ffmpeg MATCH_SOURCE
					videoFileIn = "/Volumes/pods/!Future_Videos/" + fixedName + "/final/" + fixedName + "_Temp.mp4"
					videoMatchSourceFileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/final/" + fixedName + "_" + todaysDate + "_MATCH_SOURCE.mp4"
					video360FileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/final/" + fixedName + "_" + todaysDate + "_360p.mp4"
					video720FileOut = "/Volumes/pods/!Future_Videos/" + fixedName + "/final/" + fixedName + "_" + todaysDate + "_720p.mp4"
					subprocess.Popen("ffmpeg -i %s -i %s -c:v copy -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, audioFile, videoMatchSourceFileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					#ffmpeg 360
					subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v 600k -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=640:360 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, ffAudioFile, video360FileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					#ffmpeg 720 bitrate
					length = subprocess.Popen(["ffprobe", videoFileIn], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
					lStart = length.index("Duration: ") + 10
					lEnd = length.index(",", lStart)
					length = length[lStart:lEnd]
					t = datetime.datetime.strptime(length, "%H:%M:%S.%f")
					length = (60 * t.minute) + (60 * t.hour) + t.second
					bitRate = str((802816 / length) - 320) + "k"
					#ffmpeg 720
					subprocess.Popen("ffmpeg -i %s -i %s -c:v libx264 -b:v %s -preset veryslow -profile:v baseline -g 150 -vf unsharp -vf scale=1280:720 -strict -2 -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [videoFileIn, ffAudioFile, bitRate, video720FileOut])),stdout=subprocess.PIPE,
										shell=True).communicate()[0]
					subprocess.Popen("cp %s %s" % tuple(map(pipes.quote, [video360FileOut, deliveryFolder])),
									shell=True)
					subprocess.Popen("cp %s %s" % tuple(map(pipes.quote, [video720FileOut, deliveryFolder])),
									shell=True)
					recipient = 'megan.denbow@studiesweekly.com,alex.rivera@studiesweekly.com'
					subject = 'POD Video Complete'
					body = 'A new POD video has been completed: ' + video360FileOut + ' ' + video720FileOut + ' You can find them in the !720p folder. Please QC and upload. Let Loki and Chris know if there are any issues.'
					subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(body)
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [FoldCopy2, ToDelete])),
											shell=True)
					subprocess.Popen("mv %s %s" % tuple(map(pipes.quote, [PODCopy, CompleteFolder])),
											shell=True)

#Add a failed to find folder and move WAV file here.
				#else:
				#	audioFile = FromAudio + item
				#	subprocess.Popen("cp %s %s" % tuple(map(pipes.quote, [audioFile, NotProcessed])),
				#					shell=True)#