from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class ProfileSignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50, required=True)
  email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

  class Meta:
    model = Profile
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'password1',
      'password2'
    ]


class ProfileChangeForm(UserChangeForm):

  class Meta:
    model = Profile
    fields = ('username', 'email')