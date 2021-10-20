from autoslug.fields import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=CASCADE,
        primary_key=True
    )
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=255, blank=True)
    beginn = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    nickname = models.CharField(max_length=250, blank=True)   
    short_text = models.TextField(blank=True, null=True)
    img_1 = models.ImageField(upload_to="img_uploaded/", blank=True, null=True)
    img_2 = models.ImageField(upload_to="img_uploaded/", blank=True, null=True)
    img_3 = models.ImageField(upload_to="img_uploaded/", blank=True, null=True)
    vid_1 = models.FileField(upload_to="vid_uploaded/", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)