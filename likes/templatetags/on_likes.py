from django import template
from likes import models as like_models
from posts import models as post_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_likes(context, post):
    user = context.request.user
    if user:
        try:
            the_list = like_models.Like.objects.get(user=user, name="My likes")
            return post in the_list.posts.all()
        except   like_models.Like.DoesNotExist:
            return  False
    

    
