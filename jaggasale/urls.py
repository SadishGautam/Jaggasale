from django.urls import path, include
from .views import HomeView
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', views.signup, name='signupPage'),
    path('profile', views.profilepage, name='user profile'),
    path('userPropertyList', views.userPropertyList, name="user property lists"),
    # path('about', views.about, name='about page'),
    # path('news', views.news, name='news page'),
    # path('contact', views.contact, name='contact page'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('welcome', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('property/<int:id>', views.handleDetails, name='detailed page'),
    path('Add-property', views.Add_property_by_user, name='add property'),
    path('kathmandu', views.locationKathmandu, name='Kathmandu'),
]
