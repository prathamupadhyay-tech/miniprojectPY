from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("insert/" , views.InsertData , name = "insert"),
    path("register" , views.registerView,name="register"),
    path("loginpage/" , views.LoginPage , name="LoginPage"),
    path("loginuser/" , views.LoginUser, name="login"),
    path("voice/" , views.AssistantVoice , name="voice_script"),
    path("home/shirts/" , views.shirtpage, name="shirt")
]