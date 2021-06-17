from django.contrib import admin
from . import models


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    list_display = ("name", "user", "count_posts")

    search_fields = ("name",)

    filter_horizontal = ("posts",)
