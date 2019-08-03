from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'homepage/home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    form = CommentForm()
    return render(request, 'homepage/detail.html', {'post':post_detail, 'form':form})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect ('detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'homepage/post_new.html', {'form':form})

def post_edit(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect ('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homepage/post_edit.html', {'form':form})

def post_delete(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect('home')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit = False)
            comment.post =post
            comment.save()
    return redirect('detail', post_id=post.pk)

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    return redirect('detail', post_id=post.id)