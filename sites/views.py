from django.shortcuts import render
from .models import Contact, About_us, Our_team

# Creating views to render company contact information in contact us page
def contact_page(request):
    contact_details = Contact.objects.get(id=1)
    contex = {"details" : contact_details}
    return render(request, "contact.html", contex)



#
# def about_pages(request):
#     about_us = About_us.objects.all()
#     print(about_us)
#     args = {"about_us" : about_us}
#     print("About page")
#     return render(request, "about.html", args)
#



# Creating views to render company history data and our leadership section in about us page
def about_page(request):
    our_team = Our_team.objects.all()
    about_us = About_us.objects.get(id=1)
    print(our_team)
    print(about_us)
    args = {"team" : our_team,
            "about_us" : about_us
            }
    return render(request, "about.html", args)




# def news(request):
#     return render(request, "news.html")


# Create your views here.
