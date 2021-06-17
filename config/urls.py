"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from comments import views as comment_views
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", post_views.index, name="posts"),
    path("", post_views.HomeView.as_view(), name="posts"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path("", include("pages.urls")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("comment/create/<int:post>", comment_views.create_comment, name="create"),
    path("comment/<int:comment_pk>/delete/", comment_views.delete_comment, name="delete-comment"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("likes/", include("likes.urls", namespace="likes")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
