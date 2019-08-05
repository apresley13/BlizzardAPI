import requests
from pprint import pprint
import json
import urllib.parse

url = "https://us.api.battle.net/wow/guild/Stormrage/Knightmare?fields=news&locale=en_US&apikey=xxx"

querystring = {"fields":"news","locale":"en_US","apikey":"xxx","access_token":"xxx"}

headers = {
    'Cache-Control': "no-cache",
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

#d=(json.dumps(response.json(), indent=2))
#data = json.loads(response.text)
jdata = response['news']
jdatalist=[]
for x in jdata:
	jdatalist.append(x)

for j in jdatalist:
	charname = j['character']
	type = j['type']
	timestamp = j['timestamp']
	try: item = j['itemId']
	except KeyError: pass
	if type=='itemLoot':
		print(type, charname, timestamp, item)
	else:
		continue