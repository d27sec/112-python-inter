from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre
# Create your views here.

def home(request):
        all_movies = Movie.objects.all() #read the movie table into a list
        return render(request, 'index.html', {'title': 'Server Side Render', 'movies': all_movies})
        #^^^ that is server side rendered

def catalog(request):
        return render(request, 'catalog.html')

def details(request, id):
        return render(request, 'details.html')

def about(request):
        return render(request, 'about.html')

