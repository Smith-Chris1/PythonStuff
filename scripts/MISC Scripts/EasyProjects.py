import requests
import json
import csv

headers = {
    'authorization': "Basic Y2hyaXMuc21pdGhAc3R1ZGllc3dlZWtseS5jb206TW92aWVzIzEy",
    'cache-control': "no-cache",
    'postman-token': "573c6cd7-6805-73a9-41ef-6c289e635f6a"
    }

def getProjects(url):
	response = requests.get(url, headers=headers)
	data = response.json()
	#print data
	for i in data:
		#print str(i['EntityBaseID']) + " , " + str(i['Name'])
		ID = i['EntityBaseID']
		NAME = i['Name']
		write = [str(ID)] + [str(NAME)]
		print write
		writer.writerow(write)
		#getActivities(url="https://studiesweekly.go.easyprojects.net/rest/v1/projects/" + str(i['ProjectID']) + "/activities")
	return

#def getActivities(url):
#	#print url
#	#activities = requests.get(url, headers=headers)
#	#activitiesData = activities.json()
#	#print activitiesData
#	response = requests.delete("http://studiesweekly.go.easyprojects.net/rest/v1/activities/39817", headers=headers)
#	data = response.json()
#	print data
	#for i in activitiesData:
	#	if str(i['Name']) == "Edit Reviewed" or str(i['Name']) == "Edit Locked" or str(i['Name']) == "Graphics" or str(i['Name']) == "Colored" or str(i['Name']) == "Sent to Audio" or str(i['Name']) == "Mix Returned" or str(i['Name']) == "Captioned" or str(i['Name']) == "Final Reviewed" or str(i['Name']) == "Exported" or str(i['Name']) == "Uploaded":
	#		print "Deleting: " + str(i['TaskID']) + " , " + str(i['Name'])
	#		#requests.delete("http://studiesweekly.go.easyprojects.net/rest/v1/activities/"+ str(i['TaskID']))

with open('/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/projects.csv', 'rb') as f:
	data = list(csv.reader(f))
writer = csv.writer(open("/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/projects.csv", 'w'))
getProjects(url="https://studiesweekly.go.easyprojects.net/rest/v1/projects?$skip=200&$top=200")

#getActivities("test")

