from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from comments import models
from posts.models import Post
from users.models import User
from django.views.generic import FormView
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


def delete_comment(request, comment_pk):
    user = request.user
    comment = models.Comment.objects.get(pk=comment_pk)
    post_pk = comment.post.id
    if user.pk == comment.user.pk:
        models.Comment.objects.filter(pk =comment_pk).delete()
    return redirect(reverse("posts:read", kwargs={"pk": post_pk}))
    




class CommentWriteView(FormView):
    form_class = forms.CreateCommentForm
    fields = ("content",)

    def form_valid(self, form):
        comment = form.save()
        comment.user = self.request.user
        
        # comment.post =
        comment.save()
        return redirect(reverse("posts:read", kwargs={"pk": post.pk}))

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["content"].label = "댓글"
        return form
