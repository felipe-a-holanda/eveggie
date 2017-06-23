from django.contrib import admin

from .models import *



class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'restaurant', 'overall')
    list_filter = ('restaurant',)


admin.site.register(Review, ReviewAdmin)
