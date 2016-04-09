import requests

url = "https://recipes-shobr-v1.p.mashape.com/?method=GetRecipesByFreeText&q=spaghetti+med"

headers = {
    "X-Mashape-Key": "4aOVsTiSMvmshyytENEPe2siqZwEp1mslYrjsnKgUZGL5rnwoX",
    "Accept": "application/json"
  }
r = requests.get(url, headers=headers)

print r.text[4]