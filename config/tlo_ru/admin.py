from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'new', 'sale']
    list_editable = ['sale', 'new']
          



admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(ProductContactUs)
admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainPageImage)
admin.site.register(Info)
admin.site.register(Contacts)
admin.site.register(About)
