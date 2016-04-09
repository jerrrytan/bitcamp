from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'select/', views.meal_preferences_select, name='select'),
    url(r'display/', views.display_meal_plan, name='display'),
    url(r'reset/', views.reset_page, name='reset'),
]
