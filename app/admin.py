from django.contrib import admin
from .models import *

# Register your models here.
class Adminblog(admin.ModelAdmin):

    list_display = ("title", "description", "image")


admin.site.register(blog, Adminblog)
