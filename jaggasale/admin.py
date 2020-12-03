from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title',
    'price',
    'discount_price', 'area']

admin.site.register(Item)


