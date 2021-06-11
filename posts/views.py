from posts.models import Post
from users.models import User

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


def index(request):
    posts = {"posts": Post.objects.all()}
    return render(request, "list.html", posts)


def write(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        post = Post(user_id=request.user.id, title=title, content=content)
        post.save()
        return HttpResponseRedirect("/posts")
    else:
        return render(request, "write.html")


def read(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, "read.html", {"post": post})
