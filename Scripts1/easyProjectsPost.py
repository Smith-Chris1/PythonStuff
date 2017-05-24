import httplib, urllib

host = 'http://studiesweekly.go.easyprojects.net/'
url = 'rest/v1/authentication'

values = {
  'username' : 'chris.smith@studiesweekly.com',
  'password' : 'Movies#12',
  'cookie' : '.ASPHAUTH',
}

headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/x-www-form-urlencoded',
}

values = urllib.urlencode(values)

conn = httplib.HTTPSConnection(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()

data = response.read()

print 'Response: ', response.status, response.reason
print 'Data:'
print data