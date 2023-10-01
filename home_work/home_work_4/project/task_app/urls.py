from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fake_clients/<int:count>/', views.fake_clients, name='fake_clients'),
    path('fake_products/<int:count>/', views.fake_products, name='fake_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('show_products/', views.show_products, name='show_products'),
    path('update_product/', views.update_product, name='update_product'),
]
