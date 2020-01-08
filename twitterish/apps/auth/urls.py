from django.urls import path

from . import views

urlpatterns = [
  path(
        'profile/',
        auth_views.LoginView.as_view(template_name='auth/login.html'),
        path('login', views.create, name='create')
    ),
]