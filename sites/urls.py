from django.urls import path, include
from . import views
from .views import about_page
from django.contrib import admin

urlpatterns = [
path('contact', views.contact_page, name='contact us'),
path('about', views.about_page, name='about us'),
path('add-listing', views.user_profile, name='user profile'),
path('news', views.news, name='news page'),


]
