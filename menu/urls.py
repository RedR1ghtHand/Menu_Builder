from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('dishes/', views.DishListView.as_view(), name='dish_list'),
#     path('menus/', views.menu_list, name='menus'),
#     path('dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('dishes/', views.DishListView.as_view(), name='dish_list'),
    path('dishes/category/<slug:category_slug>/', views.dish_list_by_category, name='dish_list_by_category'),
    path('dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('menus/', views.menu_list, name='menus'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

