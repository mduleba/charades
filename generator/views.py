from django.shortcuts import render, redirect
from .forms import modeselect
import random

from generator.models import Movie, Game, Series

def index(request):
    if request.method == 'POST':

        standard = modeselect(request.POST)
        if standard.is_valid():

            request.session.modified = True

            if request.POST.get("movie"):
                url = 'movie/'
            if request.POST.get("series"):
                url = 'series/'
            if request.POST.get("games"):
                url = 'games/'

            return redirect(url)
        else:
            return render(request, 'generator/index.html', {'standard': standard})
    else:
        standard = modeselect()

    return render(request, 'generator/index.html',{'standard': standard})


def movie(request):
    movie = random.choice(Movie.objects.values())
    if request.method == 'POST':

        standard = modeselect(request.POST)
        if standard.is_valid():

            if request.POST.get("movie"):
                url = 'movie'

            return redirect(url)
        else:
            return render(request, 'generator/movie.html', movie)
    else:
        standard = modeselect()
    return render(request, 'generator/movie.html', movie)

def series(request):
    series = random.choice(Series.objects.values())
    if request.method == 'POST':

        standard = modeselect(request.POST)
        if standard.is_valid():

            if request.POST.get("series"):
                url = 'series'

            return redirect(url)
        else:
            return render(request, 'generator/series.html', movie)
    else:
        standard = modeselect()
    return render(request, 'generator/series.html', movie)

def games(request):
    games = random.choice(Game.objects.values())
    if request.method == 'POST':

        standard = modeselect(request.POST)
        if standard.is_valid():

            if request.POST.get("games"):
                url = 'games'

            return redirect(url)
        else:
            return render(request, 'generator/games.html', movie)
    else:
        standard = modeselect()
    return render(request, 'generator/games.html', movie)