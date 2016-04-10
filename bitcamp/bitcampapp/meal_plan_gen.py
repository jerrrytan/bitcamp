import random
import math
from bitcampapp.models import Meal
from .get_ingredients import getIngredients
from .priceme import load_recipes

NUM_MEALS = 7


def get_meal_plan(preferences, budget):
    recipes = []
    total_cost = 0
    costs = []

    recipes_to_ingredients = {}
    recipes_to_pic_urls = {}
    recipes_to_urls = {}

    while len(recipes_to_ingredients.keys()) < NUM_MEALS:
        category = random.randrange(6)
        if category == 0:
            recipe_to_ingredients, recipe_to_pic_url, recipe_to_url = getIngredients(preferences[0])
            recipes_to_ingredients.update(recipe_to_ingredients)
            recipes_to_pic_urls.update(recipe_to_pic_url)
            recipes_to_urls.update(recipe_to_url)
        elif category == 1 or category == 2:
            recipe_to_ingredients, recipe_to_pic_url, recipe_to_url= getIngredients(preferences[1])
            recipes_to_ingredients.update(recipe_to_ingredients)
            recipes_to_pic_urls.update(recipe_to_pic_url)
            recipes_to_urls.update(recipe_to_url)
        else:
            recipe_to_ingredients, recipe_to_pic_url, recipe_to_url= getIngredients(preferences[2])
            recipes_to_ingredients.update(recipe_to_ingredients)
            recipes_to_pic_urls.update(recipe_to_pic_url)
            recipes_to_urls.update(recipe_to_url)

    recipes = []
    costs = []
    recipe_pic_urls = []
    recipe_urls = []
    total_cost = 0
    print(recipes_to_pic_urls)
    for (recipe, cost) in (load_recipes(recipes_to_ingredients)).keys():
        recipes.append(recipe)
        costs.append(cost)
        recipe_pic_urls.append(recipes_to_pic_urls[recipe])
        recipe_urls.append(recipes_to_urls[recipe])
        total_cost += cost

    if total_cost/6 > budget:
        raise Exception("Insufficient Budget!")

    else:
        for (meal, cost, recipe_to_pic_url, recipe_url) in zip(recipes, costs, recipe_pic_urls,recipe_urls):
            m = Meal(meal_name=meal, meal_cost=math.floor(cost),
                     meal_url=recipe_to_pic_url, recipe_url=recipe_url)
            m.save()
