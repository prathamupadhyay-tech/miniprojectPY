from email import message
from logging.config import listen
from django.shortcuts import render
from .models import *
import speech_recognition as sr
import pyttsx3

# Create your views here.
def registerView(request):
    return render(request , 'app/register.html')


def InsertData(request):
    #data come from HTML to view
    if request.method == "POST":
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        gender = request.POST['gender']
        uname = request.POST['uname']
        fname = request.POST['fname']
        user = customer.objects.filter(email=email)
        if user:
            message = "User already exists"
            return render(request , "app/register.html" , {'msg':message})
        else:
            if password== password2:
                newuser = customer.objects.create(firstname = fname , lastname = lname , username = uname , email = email , gender=gender,password=password,password2=password2)
                message = "user regiter Successfully"

                return render(request , "app/index.html" , {'msg': message})
            else:
                message = "Password and Confirm password does not match"
                return render(request , "app/register.html", {'msg':message})
   

    

def LoginPage(request):
    return render(request , "app/index.html")


def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

       
        user = customer.objects.get(email=email)
        
        if user:
            if user.password == password:
                request.session['Firstname'] = user.firstname
                request.session['Lastname'] = user.lastname
                request.session['Email'] = user.email
                return render(request , "app/home.html")
            else :
                message = "password does not match"
                return render(request,"app/index.html" , {'msg':message})
        else:
            message = "user does not exist"
            return render(request , "app/register.html", {'msg':message})

listener = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()

def AssistantVoice(request):
    try:
        with microphone as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'shirts ' or 'shirt' in command:
                return shirtpage(request)
            else:
                return render(request , "app/home.html",{'msg': command})

            

    except:
        return render(request , "app/home.html")

def shirtpage(request ):
    return render(request , "app/shirts.html")


