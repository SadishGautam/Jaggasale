from django.contrib import admin
from .models import Item, Images
from import_export.admin import ImportExportActionModelAdmin


class ItemImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title','price','location', 'area', 'label', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ItemImageInLine]

class BookAdmin(ImportExportActionModelAdmin):
    pass

# class ImagesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title', )}
#     list_display = ['id','title','price','discount_price', 'area']



# admin.site.register(Item, ItemAdmin)
admin.site.register(Images)
admin.site.register(Item, BookAdmin)
