from django.contrib import admin
from .models import Dish, DishIngredient, Category


class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'added_at', 'added_by')
    list_filter = ('category', 'added_by', 'added_at')
    search_fields = ('name', 'category__name', 'added_by__username')
    inlines = [DishIngredientInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

