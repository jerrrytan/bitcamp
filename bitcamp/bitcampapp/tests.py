from django.test import TestCase
import meal_plan_gen
import random

# Create your tests here.


class MealPlanGenTest(TestCase):

    def test_impossible_budget(self):
        pass

    def test_standard_use(self):
        preferences = ['latin', 'chinese', 'mediterranean']
        budget = 25
        random.seed(a=2)
        meal_plan = meal_plan_gen.get_meal_plan(preferences, budget)
        self.assertEqual(len(meal_plan), 7)
        print(meal_plan)
