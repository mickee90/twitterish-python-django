from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from django.conf import settings
from django.templatetags.static import static

class Profile(AbstractUser):
  #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  avatar = models.ImageField(blank=True, upload_to='avatars', default='avatars/avatar_default.png')

  def get_avatar(self):
    return settings.MEDIA_URL + self.avatar.name

  #def __str__(self):
    #return self.name