from urllib.request import urlopen
import json
import re
def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/'))
    print ('Raw data:',data)
    return re.compile(r'(\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
print ("response:",response)
data = json.load(str(response))
print ("json loaded data:",data)
location = str(data['loc'])
list = []
for i in location.split(','):
    list.append(i)
latitude = list[0]
longitude = list[1]
print ("Latitude : ",latitude)
print ("Longitude:" ,longitude)

