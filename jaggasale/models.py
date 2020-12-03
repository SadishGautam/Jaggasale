from django.db import models
from django.contrib.auth.models import User


CATEGORY_LIST = (
    ('H', 'House'),
    ('A', 'Apartment'),
    ('L', 'Land'),

)

LABEL_LIST = (
    ('A', 'Active'),
    ('R', 'Rent'),
    
)



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_LIST ,max_length=2, default='SOME STRING')
    label = models.CharField(choices=LABEL_LIST ,max_length=2, default='SOME STRING')
    picture_count = models.IntegerField()
    area = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    rooms = models.IntegerField()
    image = models.ImageField(default='defeult.jpg', upload_to='static/images')
    objects = models.Manager()

    def __str__(self):
        return self.title
    


def __str__(self):
    return self.user.username