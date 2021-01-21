from django.contrib import admin
from .models import Contact, About_us, Our_team

class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','phone_number',  'location']

class About_usAdmin(admin.ModelAdmin):
    list_display = ['title', ]

class Our_teamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', ]
    # readonly_fields = ('image_tag',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(About_us, About_usAdmin)
admin.site.register(Our_team, Our_teamAdmin)
