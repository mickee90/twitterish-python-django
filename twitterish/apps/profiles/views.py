from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import SignUpForm
from profiles.model import profile

class UserSignUpView(CreateView):
  model = profile
  form_class = SignUpForm
  template_name = 'auth/signup.html'

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)

    return redirect('index')