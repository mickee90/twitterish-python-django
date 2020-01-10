from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('create', views.create, name='create')
]
