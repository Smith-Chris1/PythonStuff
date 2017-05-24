import csv
from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir("/Volumes/videos/videos/!720p/!SPA") if isfile(join("/Volumes/videos/videos/!720p/!SPA", f))]
#writer = csv.writer(open("/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/720spa.csv", 'w'))
#for f in onlyfiles:
#	if f.startswith('POD'):
#		if "720p" in f:
#			size = "_720p"
#		if "360p" in f:
#			size = "_360p"
#		filename = f.rsplit("_")[4] + size +"_SPA"
#		writer.writerow([str(filename)])
#		print filename

writer = csv.writer(open("/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/names.csv", 'w'))

with open('/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/s3mp4.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='/', quotechar='|')
	for row in spamreader:
		if row[6].startswith('pod_video'):
			filename = row[6].replace('.mp4','')
			filename = filename.replace('_FINAL','')
			#filename = filename.replace('720p','')
			#filename = filename.replace('360p','')
			filename = filename.replace('pod_videos_','')
			filename = filename.replace('pod_video_','')
			writer.writerow([str(filename)])
			print filename
		else:
			filename = row[6].replace('.mp4','')
			filename = filename.replace('_FINAL_','')
			#filename = filename.replace('720p','')
			#filename = filename.replace('360p','')
			writer.writerow([str(filename)])
			print filename

with open('/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/s3mp4_newNamingConvention.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='/', quotechar='|')
	for row in spamreader:
		lang = row[6].rsplit("_")[6]
		if "SPA" in lang:
			lang = "_SPA"
		if "ENG" in lang:
			lang = ""
		filename = row[6].rsplit("_")[4]
		if "720p" in row[6]:
			size = "_720p"
		if "360p" in row[6]:
			size = "_360p"
		filename = filename + size + lang
		writer.writerow([str(filename)])