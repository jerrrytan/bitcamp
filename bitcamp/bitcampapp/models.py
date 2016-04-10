from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    meal_cost = models.IntegerField(default=10)

    def __str__(self):
        return self.meal_name
