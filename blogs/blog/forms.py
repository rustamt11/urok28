from django import forms

from blog.models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','post_title','post_text']
