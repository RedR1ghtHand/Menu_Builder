from django.shortcuts import render
from .models import Dish, Menu, Category

from django.views.generic.list import ListView


def home(request):
    return render(request, 'home.html')


def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})


class DishListView(ListView):
    model = Dish
    template_name = 'dishes.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Dish.objects.filter(category__name=category)
        else:
            return Dish.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def dish_list_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    dishes = Dish.objects.filter(category=category)
    return render(request, 'dishes.html', {'dishes': dishes})


def dish_detail(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    return render(request, 'dish_detail.html', {'dish': dish})
