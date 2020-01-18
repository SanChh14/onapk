from django.shortcuts import render, get_object_or_404
from gamesblog.models import Gamesblog
from appsblog.models import Appsblog
from itertools import chain
from operator import attrgetter
from .models import Tutorials
from django.core.paginator import Paginator

# Create your views here.

def tutorials(request):
    apps= Appsblog.objects.all()
    games = Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    tutorials = Tutorials.objects.all()
    paginator = Paginator(tutorials, 5)
    page = request.GET.get('page')
    tutorials = paginator.get_page(page)
    return render(request, 'tutorials/tutorials.html', {'tutorials': tutorials, 'trendings':trendings[:10]})
