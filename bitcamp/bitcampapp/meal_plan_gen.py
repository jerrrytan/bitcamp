import random
from bitcampapp.models import Meal
# import foodsort.priceme
# Import Alex's Stuff

num_meals = 7

def get_random_recipes_stub(theme):
    if theme == 'latin':
        return 'taco'
    elif theme == 'mediterranean':
        return 'olive'
    else:
        return 'eggroll'

def get_cost_stub(meal_plan):
    cost = 0
    for meal in meal_plan:
        if meal == 'taco':
            cost += 2
        elif meal == 'olive':
            cost += 5
        else:
            cost += 3

    return cost


def get_meal_plan(preferences, budget):
    overbudget = True
    while overbudget:
        meal_plan = []
        for meal in range(num_meals):
            category = random.randrange(6)
            if category == 0:
                meal_plan.append(get_random_recipes_stub(preferences[0]))
                # meal_plan.append(get_random_recipe(preferences[0]))
            elif category == 1 or category == 2:
                meal_plan.append(get_random_recipes_stub(preferences[1]))
                # meal_plan.append(get_random_recipe(preferences[1]))
            else:
                meal_plan.append(get_random_recipes_stub(preferences[2]))
                # meal_plan.append(get_random_recipe(preferences[2]))

        overbudget = get_cost_stub(meal_plan) > budget
        # overbudget = get_cost(meal_plan) > budget
    for meal in meal_plan:
        m = Meal(meal_name=meal)
        m.save()
