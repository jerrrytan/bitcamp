import random
import math
from bitcampapp.models import Meal
from .get_ingredients import getIngredients
from .priceme import load_recipes

NUM_MEALS = 7


def get_meal_plan(preferences, budget):
    print(preferences)
    recipes = []
    total_cost = 0
    costs = []

    recipes_to_ingredients = {}
    while len(recipes_to_ingredients.keys()) < NUM_MEALS:
        category = random.randrange(6)
        if category == 0:
            recipe_to_ingredients = getIngredients(preferences[0])
            recipes_to_ingredients.update(recipe_to_ingredients)
        elif category == 1 or category == 2:
            recipe_to_ingredients = getIngredients(preferences[1])
            recipes_to_ingredients.update(recipe_to_ingredients)
        else:
            recipe_to_ingredients = getIngredients(preferences[2])
            recipes_to_ingredients.update(recipe_to_ingredients)

    recipes = []
    costs = []
    total_cost = 0
    for (recipe, cost) in (load_recipes(recipes_to_ingredients)).keys():
        recipes.append(recipe)
        costs.append(cost)
        total_cost += cost

    if total_cost/6 > budget:
        raise Exception("Insufficient Budget!")

    else:
        for (meal, cost) in zip(recipes, costs):
            m = Meal(meal_name=meal, meal_cost=math.floor(cost))
            m.save()
