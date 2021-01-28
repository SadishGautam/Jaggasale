from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
# Create your models here.

class Blog_News(models.Model):
    title = models.CharField(max_length=50, default='Blog title')
    # author = models.ForeignKey('auth.User', verbose_name="Author", on_delete=models.CASCADE, default=1)
    full_news = RichTextUploadingField('Here you acn write full news')
    image = image = models.ImageField(default='default.jpg', upload_to='static/images/blog')
    date = date = models.DateField(blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.title
