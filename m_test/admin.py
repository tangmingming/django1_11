from django.contrib import admin

from .models import *
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)
