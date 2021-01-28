from django.shortcuts import render
from .models import Blog_News
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
# Create your views here.
def News(request):
    blog_news = Blog_News.objects.all()
    return render(request, "news.html", {'blog_news': blog_news})



def Full_News(request, id):
    blog_news = Blog_News.objects.all()
    news = Blog_News.objects.get(pk=id)
    count_hit = True
    return render(request, "news-detail1.html", { 'news': news, 'blog_news': blog_news })
