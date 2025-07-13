from django.shortcuts import render
from .models import Movie

def movie_list(request):
    q = request.GET.get('q')
    if q:
        movies = Movie.objects.filter(name__icontains=q)
    else:
        movies = Movie.objects.all()
    return render(request, 'core/movie_list.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'core/movie_detail.html', {'movie': movie})