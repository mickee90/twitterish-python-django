from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('posts/add_like/<int:pk>/', views.AddLikeView.as_view(), name='add_like'),
    path('posts/create_retweet/<int:pk>/', views.CreateRetweetView.as_view(), name='create_retweet'),
    path('posts/add_comment/<int:pk>/', views.AddCommentView.as_view(), name='add_comment')
]
