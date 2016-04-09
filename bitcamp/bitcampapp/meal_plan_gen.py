import random
from bitcampapp.models import Meal
# import foodsort.priceme
# Import Alex's Stuff

NUM_MEALS = 7
LIMIT_TRIES = 20

def get_random_recipes_stub(theme):
    if theme == 'Latin':
        return 'taco'
    elif theme == 'Mediterranean':
        return 'olive'
    else:
        return 'rice'

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
    print(preferences)
    overbudget = True
    meal_plan = []
    ctr = 0
    while overbudget and ctr < LIMIT_TRIES:
        meal_plan = []
        for meal in range(NUM_MEALS):
            category = random.randrange(6)
            print(category)
            if category == 0:
                print(meal_plan)
                meal_plan.append(get_random_recipes_stub(preferences[0]))
                # meal_plan.append(get_random_recipe(preferences[0]))
            elif category == 1 or category == 2:
                print(meal_plan)
                meal_plan.append(get_random_recipes_stub(preferences[1]))
                # meal_plan.append(get_random_recipe(preferences[1]))
            else:
                print(meal_plan)
                meal_plan.append(get_random_recipes_stub(preferences[2]))
                # meal_plan.append(get_random_recipe(preferences[2]))

        overbudget = get_cost_stub(meal_plan) > budget
        ctr += 1
        # overbudget = get_cost(meal_plan) > budget

    for meal in meal_plan:
        m = Meal(meal_name=meal)
        m.save()
