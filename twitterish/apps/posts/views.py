from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .models import Post

@login_required
def index(request):

    context = {
        'user': request.user,
        'posts': Post.objects.order_by('-created')
    }

    return render(request, 'posts/list.html', context)

@login_required
def create(request):

    post = Post(content=request.POST['content'], updated=timezone.now(), user_id=request.user.id)
    post.save()

    return HttpResponseRedirect(reverse('posts:index'))
