"""
priceme.py

There are three functions in here that will match recipes with price tags
"""
import re
from fractions import Fraction

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

def load_recipes(recipes,name="pricelist.csv"):
    """
    Takes a dictionary of recipes that maps to lists of tuples containing
    (item, amount) **update as needed**
    For each ingredient, split by words, match as many items possible against
    each item in the price list. The item with the most matches will be used.
    The updated tuple will be (item,amount,price)
    """
    ingredients = load_price_csv(name)
    new_r = {}
    final_r = {}
    for r in recipes:
        new_r[r] = []
        for item in recipes[r]:
            s = item.lower().split()[2:]
            count_l = {}
            for ing in ingredients:
                t = ing.lower().split()
                for i in t:
                    if not ing in count_l:
                        count_l[ing] = 0
                    if i in s:
                        count_l[ing] = count_l[ing] + 1
            itm,m = max(count_l,key = lambda i: count_l[i]),max(count_l)
            #A default value to indicate more is needed
            if m == 0:
                itm = item
                new_r[r].append((itm,item.split()[0],(0.00,"")))
            else:
                 new_r[r].append((itm,item.split()[0],ingredients[itm]))

    for r in new_r:
        price = 0.0
        for i in new_r[r]:
            try:
                price = price +min(5.0, float(sum(Fraction(s) for s in i[1].split("[-]*|ml|g|L")))) * i[2][0]
            except Exception:
                pass
        final_r[(r,price)] = new_r[r]
    return final_r


