from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField

from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
# from django.shortcuts import get_object_or_404


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


PROPERTY_FOR =(
    ('sold', 'SOLD'),
    ('rent', 'RENT'),
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
    sold_or_rent = models.CharField(
        choices=PROPERTY_FOR, max_length=4, default='SOLD')
    picture_count = models.IntegerField()
    area = models.IntegerField(blank=True, null=True)
    owner_name = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, default='+977 9845900495')
    date = models.DateField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    Description = RichTextUploadingField()
    location = models.CharField(
        choices=LOCATION_LIST, max_length=2, default='Kathmandu')
    map = models.CharField(max_length=150,blank=True, null=True)
    date = date = models.DateField(blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
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
