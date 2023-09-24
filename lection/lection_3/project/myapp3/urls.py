from django.urls import path
from . import views

urlpatterns = [
    path('index_init/', views.index_init, name='index_init'),
    path('hello_class/', views.HelloView.as_view(), name='HelloView'),
    # path('post/<int:year>/', views.year_post, name='year_post'),
    # path('post/<int:year>/<int:month>/', views.MonthPost.as_view(), name='month_post'),
    # path('post/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('john', views.my_view, name='index'),
    path('if/', views.TemplIf.as_view(), name='templ_if'),
    path('for/', views.view_for, name='view_for'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('autor/<int:author_id>/', views.author_posts, name='autor_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
]
