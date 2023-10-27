from django.contrib import admin
from .models import Ingredient, Category


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_of_measurement', 'added_by', 'added_at', 'category')
    list_filter = ('unit_of_measurement', 'added_by', 'added_at')
    search_fields = ('name', 'unit_of_measurement', 'added_by__username')
    date_hierarchy = 'added_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

