from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'

CATEGORY_LIST = (
    ('H', 'House'),
    ('A', 'Apartment'),
    ('L', 'Land'),

)

LABEL_LIST = (
    ('A', 'Active'),
    ('R', 'Rent'),

)

LOCATION_LIST = (
('K', 'Kathmandu'),
('L', 'Lalitpur'),
('L', 'Bhaktapur'),
('L', 'Chitwan'),

)


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
    rooms = models.IntegerField()
    Description = models.CharField(max_length=1000)
    location = models.CharField(choices=LOCATION_LIST, max_length=2, default='Kathmandu')
    map = models.CharField(max_length=150)
    image = models.ImageField(default='defeult.jpg', upload_to='static/images')
    objects = models.Manager()

    def __str__(self):
        return self.title


def __str__(self):
    return self.user.username
