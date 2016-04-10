
import requests
import json
import random

def getIngredients(genre):

    #Access edamam API data
    url = "https://edamam-recipe-search-and-diet-v1.p.mashape.com/search?_app_id=2a7c2865&_app_key=9a3f87c1707e67f965284ca3eb613dae&q="+genre
    headers = {
        "X-Mashape-Key": "GgV2guTBbhmsh0sMA33KSrcMjuyMp1EqLsPjsnZlRHycWvV5Pt",
        "Accept": "application/json"
    }
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)

    ingredients = list()
    book = {}
    book2 = {}

    #Generate random recipe
    num = random.randint(0, len(j['hits'])-1)

    #Access all ingredients for random recipe
    for i in j['hits'][num]['recipe']['ingredientLines']:
        ingredients.append(i)
    book[j['hits'][num]['recipe']['label']] = ingredients
    pic = j['hits'][num]['recipe']['image']
    book2[j['hits'][num]['recipe']['label']] = pic

    return book, book2

