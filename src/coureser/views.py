from django.shortcuts import render, get_object_or_404

# Create your views here.

from coureser.models import Film


def index(request):
    context = {
        'new_films': Film.objects.new_top(),
        'most_commented': Film.objects.most_commented(),
    }
    return render(request, 'index.html', context=context)

def film(request, fid):
    film = get_object_or_404(Film, pk=fid)
    return render(request, 'film.html', {'film': film})
