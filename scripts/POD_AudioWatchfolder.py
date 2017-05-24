import sys
import time
import gspread
import json
import datetime
from email.mime.text import MIMEText
import subprocess
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from oauth2client.service_account import ServiceAccountCredentials

now = datetime.datetime.now()
todaysDate = now.strftime("%m/%d/%Y")
#scope = ['https://spreadsheets.google.com/feeds']
#json_key = json.load(open('/Users/chrissmith/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json'))
#credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/chrissmith/Desktop/POD_Workflow_Files/Workflow-aa96f264017c.json', scope)
#gc = gspread.authorize(credentials)

#googleDoc = gc.open('Workflow Test')

#worksheet = googleDoc.worksheet("Project Tracker")

class MyHandler(PatternMatchingEventHandler):
	ignore_patterns = []
	patterns = []

	def process(self, event):
		"""
		event.event_type
			'modified' | 'created' | 'moved' | 'deleted'
		event.is_directory
			True | False
		event.src_path
			path/to/observed/file
		"""

	def on_modified(self, event):
		self.process(event)

	def on_created(self, event):
		print "Audio File Found"
		fileSource = event.src_path
		fileDestination = fileSource.replace('/Volumes/audio_recordings/PODRecordings/VoiceOverCompleted/', 'test')
		print fileDestination
		#shutil.copy2(file, '/new/dir')


if __name__ == '__main__':
	args = sys.argv[1:]
	observer = Observer()
	observer.schedule(MyHandler(), path='/Volumes/audio_recordings/PODRecordings/VoiceOverCompleted/', recursive=False)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
			observer.stop

	observer.join()