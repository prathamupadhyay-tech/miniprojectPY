from email import message
from logging.config import listen
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
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
                message = "user regitered Successfully"

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


#list of all the reachable items

products = ['home','women','men','mens','womens',"men's", "women's",'shirts','shirt' ,'mens shirt' , 'men shirt' , 'mens shirts' , 'men shirts','mens tshirt' , 'men tshirt' , 'mens tshirts' , 'men tshirts' ,'womens shirt' , 'women shirt' , 'womens shirts' , 'women shirts' ,'womens tshirt' , 'women tshirt' , 'womens tshirts' , 'women tshirts' , 'red' , 'blue' , 'green']

def searchRequest(request):
    if request.method == 'GET':
        if 'transcript' in request.GET:
            transcript = request.GET['transcript']
            # doSomething with pieFact here...
            transcript_to_be_searched = list(transcript.split(" "))

            item_to_be_searched= checkList(transcript_to_be_searched)
            item_to_be_searched = list(item_to_be_searched)
            listToStr_transcript_to_be_passed = ' '.join([str(elem) for elem in item_to_be_searched])
            if True:
                print(listToStr_transcript_to_be_passed)
                print(transcript_to_be_searched)
                print(item_to_be_searched)
                return HttpResponse(listToStr_transcript_to_be_passed)
            else:     
                print(transcript)
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')

def shirtspage(request):
    
    return render(request,"app/shirts.html")

def womenshirtspage(request):
    return render(request,"app/womenShirts.html")

def homepage(request):
    return render(request , "app/home.html" )

def checkList(transcript):
    length_of_the_transcript= len(transcript)
    for item in transcript:
        for product in products:
            if(item == product):
                yield product
                continue
            elif(item!=product):
                continue
            else:
                return product

