
import requests
import json

def getIngredients(j):

    ingredients = list()
    book = {}
    for num in range(0,5):
        ingredients.clear()
        for i in j['hits'][num]['recipe']['ingredientLines']:
            ingredients.append(i)
        book[j['hits'][num]['recipe']['label']] = ingredients

    for i in book.keys():
        print(i)
        for k in book[i]:
            print(k)

    return book


def accessRecipes(genre):

    url = "https://edamam-recipe-search-and-diet-v1.p.mashape.com/search?_app_id=2a7c2865&_app_key=9a3f87c1707e67f965284ca3eb613dae&q="+genre
    headers = {
        "X-Mashape-Key": "GgV2guTBbhmsh0sMA33KSrcMjuyMp1EqLsPjsnZlRHycWvV5Pt",
        "Accept": "application/json"
    }
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)

    ingredients = getIngredients(j)

    #print (j['hits'].recipe)
    return


 #   r = requests.get(url)



getRecipes("chinese")