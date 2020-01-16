from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('posts/add_like/<int:pk>/', views.AddLikeView.as_view(), name='add_like'),
    path('posts/create_retweet/<int:pk>/', views.CreateRetweetView.as_view(), name='create_retweet'),
    path('posts/store_comment/<int:pk>/', views.StoreCommentView.as_view(), name='store_comment')
]
