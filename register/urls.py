from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("insert/" , views.InsertData , name = "insert"),
    path("register" , views.registerView,name="register"),
    path("loginpage/" , views.LoginPage , name="LoginPage"),
    path("loginuser/" , views.LoginUser, name="login"),
    path("search/" , views.searchRequest, name="search"),
    path("shirts/" , views.shirtspage , name="shirts"),
    path("womenshirts/" , views.womenshirtspage , name="womenshirts"),
    path("" , views.homepage, name="homepage" )
]