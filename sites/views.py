from django.shortcuts import render
from .models import Contact, About_us, Our_team


def contact_page(request):
    contact_details = Contact.objects.get(id=1)
    contex = {"details" : contact_details}
    return render(request, "contact.html", contex)




def about_page(request):
    about_us = About_us.objects.all()

    args = {"about_us" : about_us}
    print("About page")
    return render(request, "about.html", args)





def about_page(request):
    our_team = Our_team.objects.all()
    print(our_team)
    args = {"team" : our_team}
    return render(request, "about.html", args)



def user_profile(request):
    return render(request, 'user_profile.html')

def news(request):
    return render(request, "news.html")


# Create your views here.
