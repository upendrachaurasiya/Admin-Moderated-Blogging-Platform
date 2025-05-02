from django.contrib import admin
from .models import UserBlog,PublicBlog

# Register your models here.
@admin.register(UserBlog)
class UserBlogAdmin(admin.ModelAdmin):
    list_display =["id","blog_user","blog_title","blog_description","blog_photo"]

@admin.register(PublicBlog)
class PublicBlogAdmin(admin.ModelAdmin):
    list_display = ["id","user","title","description","photo"]