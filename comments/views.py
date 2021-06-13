from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from posts.models import Post
from users.models import User
from comments.models import Comment
from posts import models as post_models
from django.shortcuts import render, redirect, reverse
from . import forms


def create_comment(request, post):

    if request.method == "POST":
        form = forms.CreateCommentForm(request.POST)
        post = post_models.Post.objects.get(pk=post)

        comment = form.save()
        comment.post = post
        comment.user = request.user
        comment.save()

        return redirect(reverse("posts:read", kwargs={"pk": post.pk}))
