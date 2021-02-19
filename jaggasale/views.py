from math import ceil
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Item, Images
from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import DetailView, ListView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Item
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
# from .filters import ItemFilter


class HomeView(ListView):
    model = Item
    # category = Item.objects.all()
    # category_type = Item.objects.filter()
    template_name = 'index.html'

# def Home(request):
#     return render(request, "index.html")


def signup(request):
    return render(request, "registerform.html")

def Login(request):
    return render(request, "login.html")








def profilepage(request):
    return render(request, 'profile.html')


def userPropertyList(request):
    return render(request, 'userPropertyLists')




def handleDetails(request, id):
    #fetch the property using id
    propertyLists = Item.objects.all()
    propertyList = Item.objects.get(pk=id)
    print(propertyList)
    count_hit = True
    # propertyImages = Images.objects.filter(imageitem_id= id)
    propertyImages = Images.objects.filter(imageitem_id = id)
    print(propertyImages)
    contex = {'propertyList' : propertyList,
            'propertyImages' : propertyImages
            }
    return render(request, "details.html", contex)




def SearchResultsView(request):
    query = request.GET.get('search', '')
    Title = Item.objects.filter(title__icontains=query)
    categories = Item.objects.filter(category)
    contex = { 'Title': Title,
                'categories': categories

    }
    return render(request, 'search_results.html', contex)



def handleProperty(request):
    return render(request, "details.html")




def location_properties_by_cities(request):
    query = request.GET.get('q')
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location = query)
    return render(request, "location.html", {'cities' : cities})


def locationProperties(request):
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location='K')
    return render(request, "kathmandu.html", {'cities' : cities})





@login_required
def Add_property_by_user(request):
    return render(request, "Add_apartment.html")

def handleSignup(request):
    if request.method == 'POST':
        # Get the POST parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for validation
        if len(username) > 6:
            messages.error(
                request, 'Username must be at least 6 character long')
            return HttpResponse('username must be 6 character long')

        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return HttpResponse('username format error')

        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return HttpResponse('password donot match')

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

# login the user if credentials are true


def handleLogin(request):
    if request.method == 'POST':
        # Get the POST parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
# if user exists
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            print("login success")
            return render(request, "index.html")
# if user doesnot exists
        else:
            messages.error(request, "Invalid email or password")
            print("login failed")
            return redirect('news page')

    return HttpResponse('404 - Not Found')

# logout function


def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return render(request, "index.html")


# changing the user password via user
@login_required
def change_password(request):
    if request.method == 'post':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Your password was updated successfully!')
            return redirect('settings:password')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'commons/change-password.html', {'form': form})
