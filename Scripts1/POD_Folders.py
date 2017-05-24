import glob, os
import csv
import re
os.listdir
import datetime
import shutil

now = datetime.datetime.now()
destination = ("/Volumes/pods/")
todaysDate = now.strftime("%m/%d/%Y")
writer = csv.writer(open("/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/Folders.csv", 'w'))
folders = os.listdir("/Volumes/pods/!Future_Videos/")
arrayNum = 0
for file in folders:
	foundENGFinalVideo = False;
	foundENGVOaudio = False;
	foundENGMIXaudio = False;
	foundOMFENGfile = False;
	foundSPAFinalVideo = False;
	foundSPAVOaudio = False;
	foundOMFSPAfile = False;
	foundSPAMIXAudio = False;
	foundImage = False;
	writeENGFinalVideo = False;
	writeENGVOAudio = False;
	writeOMFENGfile = False;
	writeENGMIXaudio = False;
	writeImage = False;
	writeSPAFinalVideo = False;
	writeSPAVOaudio = False;
	writeOMFSPAfile = False;
	writeSPAMIXAudio = False;
	writeENGScript = False;
	writeSPAtrans = False;
	if not file.startswith('.'):
		currentFolder = "/Volumes/pods/!Future_Videos/" + file
		os.chdir(currentFolder)
		if foundENGFinalVideo == False:
			for root, dirs, files in os.walk(currentFolder):
				for video in files:
					if not video.startswith('.'):
						if video.endswith(".mp4"):
							if "MATCH_SOURCE" in video or "720p" in video and "outroslate" not in video:
								# if  "SPA" not in video or "spa" not in video:
								#print video
								foundENGFinalVideo = True;
								#print os.path.abspath(video)
			else:
				print "Found final MP4" + currentFolder + video
		# if foundSPAFinalVideo == False:
    	# 		for root, dirs, files in os.walk(currentFolder):
		# 		for video in files:
		# 			if not video.startswith('.'):
		# 				if video.endswith(".mp4"):
		# 					if "MATCH_SOURCE" in video or "720p" in video and "outroslate" not in video:
		# 						if "ENG" not in video or "eng" not in video:
		# 							print video
		# 							foundSPAFinalVideo = True;
		# 	else:
		# 		print "Found final MP4" + currentFolder
		# if foundENGVOaudio == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".wav") or audio.endswith(".aif"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						print audio
		# 						if "vo" in audio or "VO" in audio or "SPA" not in audio or "spa" not in audio:
		# 							foundENGVOaudio = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundSPAVOaudio == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".wav") or audio.endswith(".aif"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						print audio
		# 						if "vo" in audio or "VO" in audio or "SPA" in audio or "spa" in audio:
		# 							foundSPAVOaudio = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundENGMIXaudio == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".wav") or audio.endswith(".aif"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						print audio
		# 						if "mix" in audio or "MIX" in audio:
		# 							if "spa" not in audio or "SPA" not in audio:
		# 								foundENGMIXaudio = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundSPAMIXAudio == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".wav") or audio.endswith(".aif"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						print audio
		# 						if "mix" in audio or "MIX" in audio:
		# 							if "spa" in audio or "SPA" in audio:
		# 								foundSPAMIXAudio = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundOMFENGfile == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".omf"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						print audio
		# 						if "spa" not in audio or "SPA" not in audio:
		# 							foundOMFENGfile = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundOMFSPAfile == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for audio in files:
		# 			if not audio.startswith('.'):
		# 				if audio.endswith(".omf"):
		# 					fileStart = audio.rsplit("_")[0]
		# 					music = re.search(r"[a-zA-Z]", fileStart)
		# 					if music != None:
		# 						if "spa" in audio or "SPA" in audio:
		# 							print "Audio file is: " + audio
		# 							foundOMFSPAfile = True;
		# 	else:
		# 		print "Found audio files" + currentFolder
		# if foundImage == False:
		# 	for root, dirs, files in os.walk(currentFolder):
		# 		for image in files:
		# 			if not image.startswith('.'):
		# 				if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg"):
		# 					if "BUG" not in image and "Introslate" not in image and "GuideLines" not in image and "outroslate" not in image:
		# 						print image
		# 						foundImage = True;
		# 	else:
		# 		print "Found image files" + currentFolder

		if foundENGFinalVideo == False:
			writeENGFinalVideo = ""
		else:
			writeENGFinalVideo = todaysDate
			# print video
			# print os.path.abspath(video)
			# fileSize = os.path.getsize(os.path.abspath(video))
			# print fileSize
		# if foundENGVOaudio == False:
		# 	#writeENGVOAudio = "False"
		# 	writeENGVOAudio = ""
		# 	writeENGScript = ""
		# else:
		# 	#writeENGVOAudio = "True"
		# 	writeENGVOAudio = todaysDate
		# 	writeENGScript = todaysDate
		# if foundENGMIXaudio == False:
		# 	writeENGMIXaudio = ""
		# else:
		# 	writeENGMIXaudio = todaysDate
		# if foundOMFENGfile == False:
		# 	writeOMFENGfile = ""
		# else:
		# 	writeOMFENGfile = todaysDate
		# if foundSPAFinalVideo == False:
		# 	writeSPAFinalVideo = ""
		# else:
		# 	writeSPAFinalVideo = todaysDate
		# if foundSPAVOaudio == False:
		# 	writeSPAVOaudio = ""
		# 	writeSPAtrans = ""
		# else:
		# 	writeSPAVOaudio = todaysDate
		# 	writeSPAtrans = todaysDate
		#if foundOMFSPAfile == False:
		#	#writeOMFSPAfile = "False"
		#else:
		#	#writeOMFSPAfile = "True"
		#if foundSPAMIXAudio == False:
		#	#writeSPAMIXAudio = "False"
		#else:
		#	writeSPAMIXAudio = "True"
		# if foundImage == False:
		# 	writeImage = ""
		# else:
		# 	writeImage = todaysDate

		# two = str(currentFolder).rsplit("_")[2]
		# three = str(currentFolder).rsplit("_")[3]
		# four = str(currentFolder).rsplit("_")[4]
		# projname = str(currentFolder).rsplit("_")[5]
		# six = str(currentFolder).rsplit("_")[6]
		#if str(currentFolder).rsplit("_")[7] == None:
		#	seven = ""
		#else:
		#	seven = str(currentFolder).rsplit("_")[7]

		# write = [str(projname)] + [str(three)] + [str(two)]  + [str(four)] + [str(six)] + ["POD_"+ str(two) + "_" + str(three) + "_" + str(four) + "_" + str(projname) + "_" + str(six) ] + ["111111"] + [""] + [""] + [str(writeENGScript)] + [""] + [""] + [str(writeENGVOAudio)] + ["NA"] + [""] + [str(writeSPAtrans)] + [""] + [str(writeSPAVOaudio)] + [""] + [str(writeSPAVOaudio)] + [""] + [str(writeImage)] + [""] + [""] + [""] + [""] + [str(writeOMFENGfile)] + [str(writeENGMIXaudio)] + [""] + [""] + [""] + [""] + [str(writeENGFinalVideo)] + [str(writeSPAFinalVideo)]
		# print write
		#write = [str(currentFolder)] + ["English audio VO = " + str(writeENGVOAudio)] + ["Research Completed = " + str(writeImage)] + ["English OMF = " + str(writeOMFENGfile)] + ["English MIX = " + str(writeENGMIXaudio)] + ["English Video Final = " + str(foundENGFinalVideo)] + ["Spanish audio VO = " + str(writeSPAVOaudio)] + ["Spanish OMF = " + str(writeOMFSPAfile)] + ["Spanish Mix = " + str(writeSPAMIXAudio)] + ["Spanish Video Final = " + str(writeSPAFinalVideo)]
		# writer.writerow(write)
		# if os.path.isdir(destination + "POD_" + str(two) + "_" + str(three) + "_" + str(four) + "_" + str(projname) + "_" + str(six)) == True:
		# 	print "duplicate folder"
		# else:
			#print destination + "POD_" + str(two) + "_" + str(three) + "_" + str(four) + "_" + str(projname) + "_" + str(six)
			# shutil.move(str(currentFolder), destination)
		#write = None#