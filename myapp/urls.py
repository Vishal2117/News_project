from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('politics',views.politics),
    path('sports',views.sports),
    path('technology',views.tech),
    path('world', views.world),
    path('local', views.local),
    path('search', views.search),

]