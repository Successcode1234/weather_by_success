
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    google = models.BooleanField(default=False)
    facebook = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True) 
    profile_pic_url = models.URLField(blank=True, null=True)

    # You can add more fields later 

    def __str__(self):
        return self.username or self.email
