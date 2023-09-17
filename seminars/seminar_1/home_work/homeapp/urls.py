from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('dice/', views.dice, name='dice'),
    path('rand_num/', views.random_num, name='random_num'),
]