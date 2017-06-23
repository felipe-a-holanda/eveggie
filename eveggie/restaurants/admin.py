from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)

    filter_horizontal = ('ingredients',)

admin.site.register(Ingredient)
admin.site.register(Restaurant)
admin.site.register(Town)
admin.site.register(Product, ProductAdmin)
