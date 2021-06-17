from django import template
from likes import models as like_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_likes(context, post):
    user = context.request.user
    
    the_list = like_models.Like.objects.get(user=user, name="My likes")
    return post in the_list.posts.all()
