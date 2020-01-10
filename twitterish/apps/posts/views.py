from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .models import Post

@login_required
def index(request):

    context = {
        'posts': Post.objects.order_by('-created')
    }

    return render(request, 'posts/list.html', context)

@login_required
def detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'posts/detail.html', context)

@login_required
def create(request):

    post = Post(content=request.POST['content'], updated=timezone.now(), user_id=request.user.id)
    post.save()

    return HttpResponseRedirect(reverse('posts:index'))
