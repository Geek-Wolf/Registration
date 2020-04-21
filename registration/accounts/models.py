from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    hostel=models.CharField(max_length=20, blank=False )
    profile_pic=models.ImageField(blank=True, default='profile_pic.png')        #python -m pip install Pillow           # TODO: 1) fill # 2) give default


    def __str__(self):
        return self.user.username
