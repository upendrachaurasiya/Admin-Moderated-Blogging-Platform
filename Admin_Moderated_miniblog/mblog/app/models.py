from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBlog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_photo = models.ImageField(upload_to="images/")
    blog_user = models.ForeignKey(User,on_delete=models.CASCADE)


class PublicBlog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="public/")
    user = models.CharField(max_length=100)

