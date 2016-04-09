import random
from bitcampapp.models import Meal
from .get_ingredients import getIngredients
from .priceme import load_recipes
# import foodsort.priceme
# Import Alex's Stuff

NUM_MEALS = 7
LIMIT_TRIES = 20


def get_meal_plan(preferences, budget):
    print(preferences)
    overbudget = True
    ctr = 0
    while overbudget and ctr < LIMIT_TRIES:
        recipes_to_ingredients = {}
        for meal in range(NUM_MEALS):
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

        recipe_to_cost = load_recipes(recipes_to_ingredients)
        overbudget = sum(recipe_to_cost.values()) > budget
        ctr += 1

    for meal in recipes_to_ingredients.keys():
        m = Meal(meal_name=meal)
        m.save()
