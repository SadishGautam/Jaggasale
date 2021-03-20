from django.urls import path, include
from .views import HomeView
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('loginSignup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('profile', views.profilepage, name='user profile'),
    # path('profile', views.user_profile, name='user_profile'),
    path('userPropertyList', views.userPropertyList, name="user property lists"),
    path('search/', views.SearchResultsView, name='property_search'),
    path('searchfilter', views.SearchFilter, name='Searchfilter'),

    path('signup', views.handleSignup, name='handleSignup'),
    path('welcome', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('property/<int:id>', views.handleDetails, name='detailed page'),
    path('Add-property', views.Add_property_by_user, name='add property'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount_property_details')),
    path('kathmandu', views.locationProperties, name='Kathmandu'),
    # path('location', views.locationProperties, name='Kathmandu'),
    path('location/<str:city>', views.location_properties_by_cities,
         name='location_properties_by_cities'),















]
