from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from itertools import chain

from .models import Post, Retweet, Comment

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.order_by('-created')
        retweets = Retweet.objects.select_related('post').order_by('-created')
        retweet_posts = []
        for retweet in retweets:
            retweet.post.set_is_retweet()
            retweet_posts.append(retweet.post)

        full_list = list(chain(posts, retweet_posts))
        full_ordered_list = sorted(full_list, key=lambda k: k.created, reverse=True)

        return full_ordered_list

@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

@method_decorator(login_required, name='dispatch')
class CreateView(generic.CreateView):
    model = Post
    success_url = reverse_lazy('posts:index')
    fields = ['content']
    template_name = ''

    def post(self, request, *args, **kwargs):
        post = Post(content=request.POST['content'], updated=timezone.now(), user_id=request.user.id)
        post.save()

        return HttpResponseRedirect(reverse('posts:index'))

@method_decorator(login_required, name='dispatch')
class AddLikeView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        post.likes = post.likes+1
        post.save()

        return HttpResponseRedirect(reverse('posts:index'))

@method_decorator(login_required, name='dispatch')
class CreateRetweetView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        retweet = Retweet(post_id=self.kwargs.get('pk'), user_id=request.user.id)
        retweet.save()

        return HttpResponseRedirect(reverse('posts:index'))

@method_decorator(login_required, name='dispatch')
class StoreCommentView(generic.DetailView):
    model = Comment
    template_name = ''
    fields = ['content']

    def post(self, request, *args, **kwargs):
        comment = Comment(content=request.POST['content'], user_id=request.user.id, post_id=self.kwargs.get('pk'))
        comment.save()

        return HttpResponseRedirect(reverse('posts:detail', args=[self.kwargs.get('pk')]))