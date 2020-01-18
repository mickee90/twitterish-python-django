from django.contrib.auth.models import AbstractUser
from django.db import models

import os
from django.conf import settings
from django.templatetags.static import static

from ..posts.models import Post

class Profile(AbstractUser):
  #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  avatar = models.ImageField(blank=True, upload_to='avatars', default='avatars/avatar_default.png')

  def get_avatar(self):
    return settings.MEDIA_URL + self.avatar.name
  
  def get_slug_field(self):
    return 'username'
  
  def tweet_counter(self):
    return Post.objects.filter(user_id=self.id).count()


  #def __str__(self):
    #return self.name