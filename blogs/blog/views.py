from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from blog.forms import PostModelForm
from blog.models import Post


def first_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def delete_post(request, id_post):
    post = get_object_or_404(Post, pk=id_post)
    if request.user.username == 'admin':
        post.delete()
    return redirect('first_page')


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('first_page')
    else:
        form = PostModelForm()
    context = {'form': form}
    return render(request, 'add_post.html', context=context)


@login_required
def like_post(request, id_post):
    post = get_object_or_404(Post, pk=id_post)
    post.post_likes += 1
    post.save()
    return render(request, 'check_post.html', {'posts': post})


def logout_view(request):
    logout(request)
    return redirect('first_page')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('first_page')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class PageLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('first_pages')
