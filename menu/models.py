from django.db import models
from django.contrib.auth.models import User
from ingredients.models import Ingredient


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredient')

    def __str__(self):
        return self.name


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount} {self.ingredient.unit_of_measurement} of {self.ingredient.name} ({self.ingredient.category}) in {self.dish.name}"


class Menu(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    composed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    dishes = models.ManyToManyField(Dish, related_name='menus')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Menu for {self.start_date} to {self.end_date}"

