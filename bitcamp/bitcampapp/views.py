from django.shortcuts import render
from . import meal_plan_gen
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from bitcampapp.models import Meal

# Create your views here.


def index(request):
    return render(request, 'bitcampapp/index.html')


def meal_preferences_select(request):
    preferences = [request.POST['p3'], request.POST['p2'], request.POST['p1']]
    budget = float(request.POST['budget'])
    meal_plan_gen.get_meal_plan(preferences, budget)
    return HttpResponseRedirect(reverse('display'))


def display_meal_plan(request):
    meal_models = Meal.objects.all()
    meal_list = []
    for meal_model in meal_models:
        meal_list.append(meal_model.meal_name)


    contexts = {'meal_plan': meal_list}
    return render(request, 'bitcampapp/display_plan.html', contexts)


def reset_page(request):
    if Meal.objects.all():
        Meal.objects.all().delete()

    return HttpResponseRedirect(reverse('index'))
