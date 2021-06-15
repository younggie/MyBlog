from django.db import models

from django.views.generic import View, FormView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from comments import forms as comment_forms
from comments.models import Comment

from . import models, forms
from django.views.generic import ListView


def index(request):
    posts = {"posts": models.Post.objects.all()}
    return render(request, "posts/card_list.html", posts)


class HomeView(ListView):
    model = models.Post
    paginate_by = 6
    # paginate_orphans = 1
    ordering = "-created_date"
    context_object_name = "posts"
    template_name = "posts/card_list.html"


def write(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        post = models.Post(user_id=request.user.id, title=title, content=content)
        post.save()
        return HttpResponseRedirect("/posts")
    else:
        return render(request, "write.html")


class PostWriteView(FormView):
    form_class = forms.WritePostForm
    template_name = "posts/write.html"
    fields = (
        "title",
        "content",
        "attach",
    )

    def form_valid(self, form):
        post = form.save()
        post.user = self.request.user
        post.save()
        return HttpResponseRedirect("/posts")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["title"].label = "제목"
        form.fields["content"].label = "내용"
        form.fields["attach"].label = "첨부파일"
        return form


def read(request, id):
    try:
        post = models.Post.objects.get(pk=id)
    except models.Post.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, "read.html", {"post": post})


class PostReadView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        post = models.Post.objects.get(pk=pk)
        form = comment_forms.CreateCommentForm()
        comments = Comment.objects.filter(post_id=pk)

        return render(
            self.request,
            "posts/read.html",
            {"post": post, "form": form, "comments": comments},
        )
