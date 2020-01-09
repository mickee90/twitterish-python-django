from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Post


def index(request):

    context = {
        'user': request.user,
        'posts': Post.objects.order_by('-created')
    }

    return render(request, 'posts/list.html', context)


def create(request):

    post = Post(content=request.POST['content'], updated=timezone.now())
    post.save()

    return HttpResponseRedirect(reverse('index'))
