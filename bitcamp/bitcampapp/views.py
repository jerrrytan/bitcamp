from django.shortcuts import render
from . import meal_plan_gen
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from bitcampapp.models import Meal
from . import banking


# Create your views here.


def index(request):
    contexts = {'curr_budget' : banking.getBankAmount() }
    return render(request, 'bitcampapp/index.html', contexts)


def meal_preferences_select(request):
    preferences = [request.POST['p3'], request.POST['p2'], request.POST['p1']]
    percent_budget_food = float(request.POST['percent'])
    print (percent_budget_food)
    budget = banking.percentFood(percent_budget_food)
    print(budget)

    # budget = float(request.POST['budget'])
    # try:
    meal_plan_gen.get_meal_plan(preferences, budget)
    return HttpResponseRedirect(reverse('display'))
    # except:
        # return HttpResponse("Insufficient funds", status=420)


def display_meal_plan(request):
    meal_models = Meal.objects.all()
    meal_list = []
    cost_list = []
    pic_url_list = []
    url_list = []
    for meal_model in meal_models:
        meal_list.append(meal_model.meal_name)
        cost_list.append(meal_model.meal_cost)
        pic_url_list.append(meal_model.meal_pic_url)
        url_list.append(meal_model.meal_url)


    if Meal.objects.all():
        Meal.objects.all().delete()

    contexts = {'meal_plan': meal_list, 'meal_costs' : cost_list,
                'pic_url_list' : pic_url_list,
                'curr_budget':banking.getBankAmount(), 'url_list' : url_list }
    return render(request, 'bitcampapp/display_plan.html', contexts)


def reset_page(request):
    if Meal.objects.all():
        Meal.objects.all().delete()

    return HttpResponseRedirect(reverse('index'))
