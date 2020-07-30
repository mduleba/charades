from django.shortcuts import render, redirect
from .forms import modeselect

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
    if request.method == 'POST':
        standard = modeselect(request.POST)
        if standard.is_valid():

            if request.POST.get("movie"):
                url = 'movie'

            return redirect(url)
        else:
            return render(request, 'generator/movie.html', {'standard': standard})
    else:
        standard = modeselect()

    return render(request, 'generator/movie.html',
                  {'standard': standard})