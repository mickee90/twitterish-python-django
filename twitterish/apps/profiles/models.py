from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
  pass
  #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  #avatar = models.ImageField(blank=True, upload_to=avatar)

  def __str__(self):
    return self.name