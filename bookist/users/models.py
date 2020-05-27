from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    location = models.CharField(max_length=255, help_text='Enter your location', blank=True)
    user_bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, help_text='Enter your location', blank=True)
    user_bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=CustomUser)