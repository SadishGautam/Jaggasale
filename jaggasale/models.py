from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


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
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
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
    Description = RichTextUploadingField()
    location = models.CharField(
        choices=LOCATION_LIST, max_length=2, default='Kathmandu')
    map = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='static/images')
    objects = models.Manager()

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="90" />'.format(self.image.url))

    image_tag.short_description = 'Image'




class Images(models.Model):
    imageitem = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    image= models.ImageField(blank= True, upload_to='static/images')

    def __str__(self):
        return self.title
