from django import forms
from . import models


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("content",)
        labels = {
            "content": "댓글쓰기",
        }

    def save(self):
        comment = super().save(commit=False)
        return comment
