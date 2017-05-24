from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
#gauth.LoadCredentialsFile("/Volumes/videos/videos/DROP_BIN/CHRIS/POD_Workflow_Files/Workflow-aa96f264017c.json")
if gauth.credentials is None:
	# Authenticate if they're not there
	gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
	# Refresh them if expired
	gauth.Refresh()
else:
	# Initialize the saved creds
	gauth.Authorize()

gauth.SaveCredentialsFile("/Volumes/videos/videos/DROP_BIN/CHRIS/POD_Workflow_Files/mycreds.txt")
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
	print('title: %s, id: %s' % (file1['title'], file1['id']))