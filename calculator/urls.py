from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("calculate", views.calculate, name='calculate'),
    path("all_pizzas", views.all_pizzas, name='all_pizzas'),
    re_path(r'^pizzas$', views.pizza_list),
]
