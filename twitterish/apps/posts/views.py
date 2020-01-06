from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):

    context = {
        'posts': Post.objects.order_by('-created')
    }

    return render(request, 'posts/list.html', context)
