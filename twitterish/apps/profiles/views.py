from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import ProfileSignUpForm
from .models import Profile


class ProfileSignUpView(CreateView):
  model = Profile
  form_class = ProfileSignUpForm
  success_url = reverse_lazy('login')
  template_name = 'auth/signup.html'

  def form_valid(self, form):
    profile = form.save()

    return HttpResponseRedirect(reverse('login'))