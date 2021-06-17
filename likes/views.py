from django.shortcuts import render
from django.shortcuts import redirect, reverse
from posts import models as post_model
from . import models



def toggle_like(request, post_pk):
    action = request.GET.get("action", None)
    post = post_model.Post.objects.get(pk=post_pk)
    if post is not None and action is not None:
        the_list, _ = models.Like.objects.get_or_create(
            user=request.user, name ="My likes"
        )
        if action == "add":
            the_list.posts.add(post)
        elif action == "remove":
            the_list.posts.remove(post)
    return redirect(reverse("posts:read", kwargs={"pk": post_pk}))

""" def save_like(request, post_pk):
    print(request.user)
    post = post_model.Post.objects.get(pk=post_pk)
    if post is not None:
        the_list, _ = models.Like.objects.get_or_create(
            user=request.user, name="My likes"
        )
        the_list.posts.add(post)
    return redirect(reverse("posts:read", kwargs={"pk": post_pk})) """