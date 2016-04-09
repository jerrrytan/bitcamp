import json
import requests

url = "https://edamam-recipe-search-and-diet-v1.p.mashape.com/search?_app_id=2a7c2865&_app_key=9a3f87c1707e67f965284ca3eb613dae&q=korean"


headers = {
	"X-Mashape-Key": "GgV2guTBbhmsh0sMA33KSrcMjuyMp1EqLsPjsnZlRHycWvV5Pt",
	"Accept": "application/json"
}
r = requests.get(url, headers=headers)
j = json.loads(r.text)

print j['hits'][0]['recipe']['ingredientLines']

for i in j['hits'][0]['recipe']['ingredientLines'] :
	print i
	
