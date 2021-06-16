from django.db import models

from django.views.generic import View, FormView,UpdateView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from comments import forms as comment_forms
from comments.models import Comment
from django.core.paginator import Paginator
from django.db.models import Q

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

class PostEditView(UpdateView):
    model = models.Post
    template_name = "posts/edit.html"
    fields = {
        "title",
        "content",
        "attach",       
    }
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["title"].label = "제목"
        form.fields["content"].label = "내용"
        form.fields["attach"].label = "첨부파일"
        return form    

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        if post.user.pk != self.request.user.pk:
            raise Http404()
        return post

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


def delete_post(request, pk):
    user = request.user
    post = models.Post.objects.get(pk=pk)
    
    if user.pk == post.user.pk:
        models.Post.objects.filter(pk =pk).delete()
    return redirect("/")


class SearchView(View):

    def get(self, request):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            search_text = form.cleaned_data.get("search_text")
            print(search_text)
            post_list = models.Post.objects.filter(Q(title__contains=search_text) | Q(content__contains=search_text))

            paginator = Paginator(post_list, 10, orphans=5)

            page = request.GET.get("page", 1)

            posts = paginator.get_page(page)



   
           

            #qs = models.Post.objects.get(title__contains=search_text)

            return render(
                    request, "posts/card_list.html", {"form": form, "posts": posts}
            )

