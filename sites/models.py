from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, default='+977 9845900495') # validators should be a list
    email = models.EmailField(max_length=70, null=False, blank=False, default='Thesadishgautam@gmail.com')
    location = models.CharField(max_length=100, default='Tinkune, KTM')
    office_days = models.CharField(max_length=100, default='Monday – Friday')
    office_time = models.CharField(max_length=100, default='10:00AM – 6:00PM')


    def __str__(self):
        return self.email


class About_us(models.Model):
    title = models.CharField(max_length=30, default='Company History')
    company_history = RichTextUploadingField()
    office_location_headquarter = RichTextUploadingField()
    office_location_lalitpur = RichTextUploadingField()
    office_location_bhaktapur = RichTextUploadingField()


    def __str__(self):
        return self.title



class Our_team(models.Model):
        name = models.CharField(max_length=30, default='Rich Wacksman')
        position = models.CharField(max_length=50, default='Chief Legal Officer')
        image = models.ImageField(default='default.jpg', upload_to='static/images')
        facebook = models.CharField(max_length=50, default='#')
        twitter = models.CharField(max_length=50, default='#')
        gmail = models.CharField(max_length=50, default='#')
        linkedin = models.CharField(max_length=50, default='#')
        instagram = models.CharField(max_length=50, default='#')
        outlook = models.CharField(max_length=50, default='#')

        def __str__(self):
            return self.name

        def image_tag(self):
            return mark_safe('<img src="{}" width="100" height="90" />'.format(self.image.url))

        image_tag.short_description = 'Image'
