from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



CATEGORY_LIST = (
    ('H', 'House'),
    ('A', 'Apartment'),
    ('L', 'Land'),

)

LABEL_LIST = (
    ('A', 'Active'),
    ('I', 'Inactive'),

)

LOCATION_LIST = (
('K', 'Kathmandu'),
('L', 'Lalitpur'),
('L', 'Bhaktapur'),
('C', 'Chitwan'),

)


class user_details(models.Model):
    """docstring for user_details."""


    def __str__(self):
        return self.user.username




class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(
        choices=CATEGORY_LIST, max_length=2, default='Error fetching category')
    label = models.CharField(
        choices=LABEL_LIST, max_length=2, default='Active')
    picture_count = models.IntegerField()
    area = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    Description = models.TextField(max_length=1000)
    location = models.CharField(choices=LOCATION_LIST, max_length=2, default='Kathmandu')
    map = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='static/images')
    objects = models.Manager()

    def __str__(self):
        return self.title
