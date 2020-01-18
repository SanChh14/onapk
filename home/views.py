from django.shortcuts import render
from appsblog.models import Appsblog
from gamesblog.models import Gamesblog
from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request):
    apps= Appsblog.objects.all()
    games= Gamesblog.objects.all()
    all = sorted(chain(apps,games),key=attrgetter('pub_date'),reverse=True)
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    paginator = Paginator(all, 5)
    page = request.GET.get('page')
    all = paginator.get_page(page)
    return render(request, 'home/index.html', {'all': all,'trendings':trendings[:10]})

def search(request):
    apps= Appsblog.objects.all()
    games= Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    query= request.GET.get("q")
    if query:
        apps = apps.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(features__icontains=query))
        games = games.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(features__icontains=query))
        all = sorted(chain(apps,games),key=attrgetter('pub_date'),reverse=True)
    else:
        all = []
    paginator = Paginator(all, 5)
    page = request.GET.get('page')
    all = paginator.get_page(page)
    return render(request, 'search.html', {'all': all,'trendings':trendings[:10]})

def about(request):
    apps= Appsblog.objects.all()
    games= Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    return render(request, 'about.html', {'trendings':trendings[:10]})
