from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
  path('<str:slug>/', views.DetailView.as_view(), name='detail')
]