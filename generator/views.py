from django.shortcuts import render, redirect
from .forms import modeselect
import random

from generator.models import Movie

def index(request):
    if request.method == 'POST':

        standard = modeselect(request.POST)
        if standard.is_valid():

            request.session.modified = True

            if request.POST.get("movie"):
                url = 'movie/'

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