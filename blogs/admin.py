from django.contrib import admin
from blogs.models import BlogsPost

# Register your models here.

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'createdate']

admin.site.register(BlogsPost, BlogsPostAdmin)

