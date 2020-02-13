from django.contrib import admin
from django.urls import path
from . import views

app_name = "fcutdsite"
 
urlpatterns = [
    path('', views.yourclub, name = "yourclub"),
    path('fixtures/', views.fixtures, name = "fixtures"),
    path('leaguetable/', views.leaguetable, name = "leaguetable"),
    path('squad/', views.squad, name = "squad"),
    path('stadium/', views.stadium, name = "stadium"),
    path('news/', views.news, name = "news"),
    path('detail/<int:id>',views.detail,name = "detail"),
]

