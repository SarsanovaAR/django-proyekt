from django.contrib import admin
from.models import *
# Register your models here.
class Postmobel(admin.ModelAdmin):

    list_display =('title','fr_content','post_date',)
    list_filter =('post_date',)

admin.site.register(Post, Postmobel)