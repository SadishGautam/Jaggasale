from math import ceil
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Item
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class HomeView(ListView):
    model = Item
    template_name = 'index.php'

def signup(request):
    return render(request, "registerform.php")


def about(request):
    return render(request, "about.php")



def news(request):
    return render(request, "news.php")

def contact(request):
    return render(request, "contact.php")

    
def handleSignup(request):
    if request.method == 'POST':
        #Get the POST parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
        #Check for validation
        if len(username) > 6:
            messages.error(request, 'Username must be at least 6 character long')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect('home')



        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.username = username
        myuser.save()
        messages.success(request, 'Your account has been created successfully')
        print("Your account has been created successfully")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        #Get the POST parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

      
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            print("login success")
            return HttpResponse('Logged in Successfully')

        else:
            messages.error(request, "Invalid email or password")
            print("login failed")
            return redirect('news page')
        

    return HttpResponse('404 - Not Found')








def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    print("logout success")
    return HttpResponse('Logged out Successfully')


def index(request):
    products = Item.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)) - (n//4)

    allprods = []
    catprods = Item.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Item.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)) - (n//4)
        allprods = [[products, range(1, len(products)), nslides],
                    [products, range(1, len(products)), nslides]]
        params = {'allprods': allprods}   
        return render(request, 'index.php', params)
        