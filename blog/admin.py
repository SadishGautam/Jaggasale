from django.contrib import admin
from .models import Blog_News
# Register your models here.
class Blog_NewsAdmin(admin.ModelAdmin):
    list_display = ['title',]

admin.site.register(Blog_News)
