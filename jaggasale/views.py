from math import ceil
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Item, Images
from math import ceil
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import DetailView, ListView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from .forms import HouseForm  # ApartmentForm
from django.forms import modelformset_factory
import requests
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.forms import ModelChoiceField

# from .filters import ItemFilter


class HomeView(ListView):
    model = Item
    def get_queryset(self, *args, **kwargs):
        qs = super(HomeView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs[:6]
    template_name = 'index.html'



#
# def Index_page(request):
#     prop = Item.objects.all()
#     print(prop)
#     return render(request, "index.html", {'prop': prop})

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def toastr(request):
    return render(request, "updateform/toastr.html")




def signup(request):
    return render(request, "registerform.html")


def Login(request):
    return render(request, "login.html")


# showing users property in profile page
@login_required(login_url="/login")
def profilepage(request):
    user_property = Item.objects.filter(user=request.user)

    return render(request, 'profile.html',
                  {'user_property': user_property}
                  )


# Adding House property by user
@login_required(login_url="/login")
def Add_property_by_user(request):
    form = HouseForm(request.POST or None, request.FILES)
    count = Item.objects.filter(user=request.user).count()

    if request.method == "POST":
        images = request.FILES.getlist('imagesss')

        if form.is_valid():
            saving = form.save(commit=False)
            print(request.user)
            # saving.Latitude =  request.POST['Latitude']
            # saving.Longitude =  request.POST['Longitude']
            # print(Latitude)
            # print(Longitude)
            saving.user = request.user
            saving.save()
            # response.user.HouseForm.add(form)
            messages.success(request, "saved")
            form = HouseForm()
        else:
            # form = HouseForm()
            messages.error(request, "Property cannot be saved")
        for image in images:
            photo = Images.objects.create(image=image, imageitem=saving)
            photo.save()
    return render(request, "Add_apartment.html", {'form': form, 'count': count})





# Deleting property by user

@login_required(login_url="/login")
def delete_property(request, id):
    id = int(id)
    try:
        user_property = Item.objects.filter(user=request.user)
        del_property = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        messages.success(request, "Error in deleting property")
    del_property.delete()
    print("deleted")
    messages.success(request, "Property deleted successfully")
    return HttpResponseRedirect("profile.html", {'del_property': del_property})
    # return render(request, 'profile.html',{'del_property': del_property})


# Updating property by user
@login_required(login_url="/login")
def update_property(request, id):
    user_property = Item.objects.filter(user=request.user)
    edit_property = Item.objects.get(pk=id)
    edit_form = HouseForm(request.POST or None,
                          request.FILES, instance=edit_property)
    edit_form = HouseForm(instance=edit_property)
    # edit_form = HouseForm(request.POST or None, instance = edit_property)
    if edit_form.is_valid():
        edit_form.cleaned_data.get('title')
        edit_form.cleaned_data.get('price')
        saving = edit_form.save()
        messages.success(request, "Property Updated successfully")

        print(request.user)
    else:
        messages.error(request, "Error in Updating property")

    contex = {'user_property': user_property,
              'edit_property': edit_property,
              'edit_form': edit_form,
              }
    # edit_form = HouseForm(instance=edit_property)
    return render(request, 'updateform/update.html', contex)


def userPropertyList(request):
    return render(request, 'userPropertyLists')


# Property detail page
def handleDetails(request, id):
    # fetch the property using id

    propertyLists = Item.objects.all()
    propertyList = Item.objects.get(pk=id)
    print(propertyList)
    count_hit = True
    property_owner_name = User.objects.get(id=propertyList.user_id)


    url = requests.get("http://127.0.0.1:5000/property?Property_ID=" + str(id))

    # propertyImages = Images.objects.filter(imageitem_id= id)
    propertyImages = Images.objects.filter(imageitem_id=id)
    pictuess_count = Images.objects.filter(imageitem_id=id).count()
    print(propertyImages)
    for i in propertyImages:
        print(i.image.url)
    response = requests.get('http://127.0.0.1:5000/recommendproperty?Property_ID='+str(id)).json()

    # print(response)
    Rec_property = ["Title", "Address"]
    category = ['catering.restaurant', 'education.school', 'healthcare.hospital']
    out = []
    latitude = propertyList.Latitude
    longitude = propertyList.Longitude
    print(latitude)



    # for i,j in enumerate(category):
    for i in category:
        a = requests.get('https://api.geoapify.com/v2/places?categories='+i+'&filter=circle:'+latitude+','+longitude+',5000&bias=proximity:'+latitude+','+longitude+'&limit=5&apiKey=a46f6787113941dabf4252d0951cd9bf')
        out.append(a.json())
    # print(out)
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            try:
                # property_user = User.objects.get(id=form.cleaned_data['to_email'])
                send_mail(full_name, message, from_email,
                          [property_owner_name.email])
            except BadHeaderError:

                messages.error(request, 'Invalid header found.')

            messages.success(request, 'Success! Thank you for your message.')
    contex = {'propertyList': propertyList,
              'propertyImages': propertyImages,
              'form': form,
              'response': response,
              'out': out,
              'url': url,
              'property_owner_name': property_owner_name,
              'pictuess_count': pictuess_count,
              }
    return render(request, "details.html", contex)


# def contactView(request, id):
#
#
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 property_user = User.objects.get(id=form.cleaned_data['to_email'])
#                 send_mail(subject, message, from_email,
#                           [property_user.email])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return HttpResponse('Success! Thank you for your message.')
#     return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def is_valid_queryparam(param):
    return param != '' and param is not None

# Search page
def SearchResultsView(request):
    # property_item = Item.objects.all()
    query = request.GET.get('search', '')
    Title = Item.objects.filter(title__icontains=query)

    minprice = request.GET.get('minprice')
    maxprice = request.GET.get('maxprice')

    if is_valid_queryparam(maxprice):
        Title = Title.filter(price__gte=minprice)

    if is_valid_queryparam(minprice):
        Title = Title.filter(price__lt=maxprice)

    new_updated_title = []
    j=0
    for i in Title:
        new_updated_title.append(i)
        j+=1
        if j>6:
            break
    contex = {'Title': new_updated_title,}

            # 'property_item':property_item,                    }
    return render(request, 'search_results.html', contex)


# def SearchFilter(request):
#     if request.method == "POST":
#         minprice = request.POST.get('minprice')
#         maxprice = request.POST.get('maxprice')
#         print(minprice)
#         print(maxprice)
#
#         filtered_search = Item.objects.raw(
#             'select id, title, price from jaggasale_item where price between "' + minprice + '" and "' + maxprice + '"')
#         return render(request, 'search_results.html', {'filtered_search': filtered_search})
#
#     else:
#         Title = Item.objects.all()
#
#         contex = {'Title': Title,
#                   # 'categories': categories
#
#                   }
#         return render(request, 'search_results.html', contex)


def handleProperty(request):
    return render(request, "details.html")


def location_properties_by_cities(request):
    query = request.GET.get('q')
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location=query)
    return render(request, "location.html", {'cities': cities})


def Kathmandu(request):
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location='Kathmandu')[:7]
    minprice = request.GET.get('minprice')
    maxprice = request.GET.get('maxprice')

    if is_valid_queryparam(maxprice):
        cities = Title.filter(price__gte=minprice)

    if is_valid_queryparam(minprice):
        cities = Title.filter(price__lt=maxprice)

    return render(request, "location/kathmandu.html", {'cities': cities})


def Lalitpur(request):
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location='Lalitpur')[:7]
    minprice = request.GET.get('minprice')
    maxprice = request.GET.get('maxprice')

    if is_valid_queryparam(maxprice):
        cities = Title.filter(price__gte=minprice)

    if is_valid_queryparam(minprice):
        cities = Title.filter(price__lt=maxprice)
    return render(request, "location/lalitpur.html", {'cities': cities})


def Bhaktapur(request):
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location='Bhaktapur')[:5]
    return render(request, "location/bhaktapur.html", {'cities': cities})


def Chitwan(request):
    Properties_by_cities = Item.objects.all()
    cities = Item.objects.filter(location='Chitwan')[:7]
    return render(request, "location/chitwan.html", {'cities': cities})


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
            return HttpResponseRedirect("/")
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
    return HttpResponseRedirect("/")
