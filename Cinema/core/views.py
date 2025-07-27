from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Movie, Comment
from .forms import CommentForm

def movie_list(request):
    q = request.GET.get('q')
    if q:
        movies = Movie.objects.filter(name_lower__icontains=q.lower())
    else:
        movies = Movie.objects.all()
    return render(request, 'core/movie_list.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', id=movie.id)
    return render(request, 'core/movie_detail.html', {'movie': movie, 'form': form})


# ========= login, logout, register =============
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth


def login(request):
    if request.user.is_authenticated:
        return redirect('movie_list')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('movie_list')


def register(request):
    if request.user.is_authenticated:
        return redirect('movie_list')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)

    if comment.user != request.user:
        return HttpResponseForbidden('Вы не можете редактировать этот комментарий!')

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', id=comment.movie.id)

    form = CommentForm(instance=comment)
    return render(request, 'core/edit_comment.html', {'comment': comment, 'form': form})