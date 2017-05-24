import csv
with open('/Users/chrissmith/Desktop/Desktop_Stuff/Scripts/s3mp4.csv', 'wb') as csvfile:
	spamwriter = csv.reader(csvfile, delimiter='_', quotechar='|')
	for row in spamreader:
	print ', '.join(row)