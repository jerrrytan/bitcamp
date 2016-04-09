"""
priceme.py

There are three functions in here that will match recipes with price tags
"""
import re

prices = {}

def load_price_csv(name="pricelist.csv"):
    """
    Takes in a list of prices delimited by commas and returns a dictionary
    with ingredient names and parsed prices in float form along with the 
    units represented by the price.
    """
    p_index = {}
    with open(name,"r") as f:
        pmatch = re.compile("(\d)*\.(\d\d)") 
        for line in f.readlines():
            s = line.split(",")
            try:
                price = float(pmatch.search(s[1]).group())
                p_index[s[0]] = (price,s[2])
            except Exception:
                pass
        return p_index

def load_recipes(recipes,ingredients):
    """
    Takes a dictionary of recipes that maps to lists of tuples containing
    (item, amount) **update as needed**
    For each ingredient, split by words, match as many items possible against
    each item in the price list. The item with the most matches will be used.
    """
    new_r = {}
    final_r = {}
    for r in recipes:  
        new_r[r] = []
        for item in recipes[r]:
            s = item[0].split()
            count_l = {}
            for ing in ingredients:
                t = ing.split()
                for i in t:
                    if not i in count_l:
                        count_l[i] = 0
                    if not re.search(i,item[0]) == None:
                        count_l[i] = count_l[i] + 1
            itm = max(count_l,key = lambda i: count_l[i])
            new_r[itm].append(itm, item[1],ingredients[itm])
    for r in new_r:
        price = 0.0
        for i in new_r[r]:
            price = price + i[1] * i[2]

        final_r[(r,price)] = new_r[r]
    return final_r
