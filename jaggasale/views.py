from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
from math import ceil
from django.views import generic
from django.http import HttpResponse


class HomeView(ListView):
    model = Item
    template_name = 'index.php'

def home(request):
  
    params = {}
    
    

    # params = {'product': products}
    



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
        