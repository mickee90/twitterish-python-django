from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ProfileSignUpForm
from .models import Profile
from ..posts.models import Post


class ProfileSignUpView(CreateView):
  model = Profile
  form_class = ProfileSignUpForm
  success_url = reverse_lazy('login')
  template_name = 'auth/signup.html'

  def form_valid(self, form):
    profile = form.save()

    return HttpResponseRedirect(reverse('login'))
  
@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
  model = Profile
  template_name = 'profiles/detail.html'
  slug_field = 'username'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['posts'] = Post.objects.filter(user_id=kwargs['object'].id)

    return context
