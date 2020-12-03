from django.urls import path
from .views import HomeView
from . import views



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', views.signup, name='signupPage'),
    path('about', views.about, name='about page'),
    path('news', views.news, name='news page'),
    path('contact', views.contact, name='Contact page'),
    path('signup', views.handleSignup, name='signup'),
]
