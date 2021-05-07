from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField

from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
# from django.shortcuts import get_object_or_404
from django.utils import timezone

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

PROPERTY_AREA_FACE=(
('E', 'East'),
('W', 'West'),
('N', 'North'),
('S', 'South'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(
        choices=CATEGORY_LIST, max_length=2, null=True, blank=True)
    area_face = models.CharField(
        choices=PROPERTY_AREA_FACE, max_length=2, null=True, blank=True)
    label = models.CharField(
        choices=LABEL_LIST, max_length=2, default='Active')
    sold_or_rent = models.CharField(
        choices=PROPERTY_FOR, max_length=4, default='SOLD')
    picture_count = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    owner_name = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=False, default='')
    built_date = models.DateField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    Description = RichTextUploadingField()
    location = models.CharField(
        choices=LOCATION_LIST, max_length=2)
    Latitude= models.CharField(max_length=25, blank=True, null=True)
    Longitude= models.CharField(max_length=25, blank=True, null=True)
    date =models.DateField(blank=True, null=True, default=timezone.now)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')


# checkbox items
    have_parking = models.BooleanField("Parking", default=False)
    have_garden = models.BooleanField("garden", default=False)
    have_drinage = models.BooleanField("drinage", default=False)
    have_balcony = models.BooleanField("balcony", default=False)
    have_hallRoom = models.BooleanField("hallRoom", default=False)
    have_diningRoom = models.BooleanField("diningRoom", default=False)
    have_elevator = models.BooleanField("elevator", default=False)
    have_water = models.BooleanField("water", default=False)

    
    have_electricityBackup = models.BooleanField("electricityBackup", default=False)
    have_securityStaff = models.BooleanField("securityStaff", default=False)
    have_lift = models.BooleanField("lift", default=False)
    have_kidsPlayground = models.BooleanField("kidsPlayground", default=False)
    have_electricityPole = models.BooleanField("electricityPole", default=False)
    have_road = models.BooleanField("road", default=False)
    have_waterSupply = models.BooleanField("waterSupply", default=False)

# Extra checkbox for apartment
    Ap_have_parking = models.BooleanField("Ap_Parking", default=False)
    AP_have_electricity = models.BooleanField("Ap_electricity", default=False)
    Ap_have_drinage = models.BooleanField("Ap_drinage", default=False)
    Ap_have_dining_room = models.BooleanField("Ap_dining_room", default=False)
    Ap_have_kids_playground = models.BooleanField("Ap_kids_playground", default=False)
    Ap_have_lift = models.BooleanField("Ap_lift", default=False)
    Ap_have_water_supply = models.BooleanField("Ap_water_supply", default=False)




# Extra checkbox for Land
    La_have_road = models.BooleanField("La_road", default=False)
    La_have_electricity = models.BooleanField("La_electricity", default=False)
    La_have_drinage = models.BooleanField("La_drinage", default=False)
    La_have_water = models.BooleanField("La_water", default=False)




    image = models.ImageField( upload_to='static/images')
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
     return reverse('CRUD_Item:Item_edit', kwargs={'pk': self.pk})

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="90" />'.format(self.image.url))

    image_tag.short_description = 'Image'


# class Propertyreturn render(request, "/")FeatureCheckbox(models.Model):
#





class Images(models.Model):
    imageitem = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30, blank=True)
    image= models.ImageField(null=True, blank= True, upload_to='static/images')


    def __str__(self):
        return self.title
