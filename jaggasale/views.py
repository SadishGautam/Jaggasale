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
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from .forms import HouseForm
# from .filters import ItemFilter


class HomeView(ListView):
    model = Item
    # category = Item.objects.all()
    # category_type = Item.objects.filter()
    template_name = 'index.html'

# def Home(request):
#     return render(request, "index.html")

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response





def signup(request):
    return render(request, "registerform.html")

def Login(request):
    return render(request, "login.html")





# ----------------user profile
# def user_profile(request):
#     user = request.user
#     user_posts = Items.objects.filter(editor=user)
#     return render(request, 'profile.html', {user_posts': user_posts})







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
    # categories = Item.objects.filter(category)
    contex = { 'Title': Title,
                # 'categories': categories

    }
    return render(request, 'search_results.html', contex)


def SearchFilter(request):
    if request.method == "POST":
        minprice = request.POST.get('minprice')
        maxprice = request.POST.get('maxprice')
        print('maxprice')
        filtered_search = Item.objects.raw('select id, title, price from jaggasale_item where price between "'+minprice+'" and "'+maxprice+'"')
        return render(request, 'search_results.html', {'filtered_search': filtered_search})

    else:
        Title = Item.objects.all()

        contex = { 'Title': Title,
                    # 'categories': categories

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
    form = HouseForm(request.POST or None, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.success(request, "saved")

         # else:
         #     form = HouseForm()
         #     messages.error(request, "Invalid email or password")
    return render(request, "Add_apartment.html", {'form': form})







def handleSignup(request):
    print("signup handle success")
    if request.method == 'POST':
        print("signup handle")

        # Get the POST parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for validation
        if len(username) > 3:
            messages.error(
                request, 'Username must be at least 3 character long')
            # return HttpResponse('username must be 3 character long')

        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            # return HttpResponse('username format error')

        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            # return HttpResponse('password donot match')

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
            return render(request, "login.html")


    return HttpResponse('404 - Not Found')

# logout function


def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return render(request, "index.html")


# Starting of adding property by user
# @login_required
# def property_create(request):
#     if request.method == 'POST':
#         form = HouseForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             House = form.save(commit=False)
#             House.user = request.user
#             House.category = request.category
#             House.save()
#             return redirect('CRUD_Item:Item_edit')
#     return render(request, 'Add_apartment.html', {'form': form})
#











    # Ending of adding property by user
