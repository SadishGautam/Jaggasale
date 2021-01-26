from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('news', views.News, name='news'),
    path('news/<int:id>', views.Full_News, name='Full news'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    # path('news/<int:id>', views.Full_News, name='Full news page'),
]
