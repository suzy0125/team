from django import forms
from .models import Post, Comment

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title' , 'brand', 'text', 'component' , 'author', 'published_date', 'photo'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nickname', 'text')