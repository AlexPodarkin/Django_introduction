from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_form_1/', views.user_form, name='user_form'),
    path('user_form_2/', views.user_form_2, name='user_form_2'),
    path('many_fields_form/', views.many_fields_form, name='many_fields_form'),
    path('add_user/', views.add_user, name='add_user'),
    path('show_users/', views.show_users, name='show_users'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('choice_user/', views.choice_user, name='choice_user'),
]
