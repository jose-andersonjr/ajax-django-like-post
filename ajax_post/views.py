from multiprocessing import context
from django.shortcuts import render
from .models import Post, Like
# Create your views here.
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context)


def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")