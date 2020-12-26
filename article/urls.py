from django.contrib import admin
from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.index,name='index'),
    path('name/', views.index,name='name'),
    path('author/', views.index,name='author'),
]
