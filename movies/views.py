from django.shortcuts import render, get_object_or_404
from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects.all()

    return render(request, 'movies/index.html', {
        'movies': movies
    })

def details(request, mov):
    movie = get_object_or_404(Movies, pk=mov)
    return render(request, 'movies/details.html', {
        'movie': movie
    })