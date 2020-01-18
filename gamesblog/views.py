from django.shortcuts import render, get_object_or_404
from .models import Gamesblog
from appsblog.models import Appsblog
from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator

# Create your views here.

def gamesblog(request):
    apps= Appsblog.objects.all()
    games = Gamesblog.objects.all().order_by('-pub_date')
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    paginator = Paginator(games, 5)
    page = request.GET.get('page')
    games = paginator.get_page(page)
    return render(request, 'gamesblog/gamesblog.html', {'games': games,'trendings':trendings[:10]})

def game_detail(request, gamesblog_id):
    apps= Appsblog.objects.all()
    games = Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    game_detail = get_object_or_404(Gamesblog, pk=gamesblog_id)
    features= list(game_detail.features.split('\n'))
    install_steps= list(game_detail.install_steps.split('\n'))
    description = list(game_detail.description.split('\n'))
    game_detail.views = game_detail.views+1
    game_detail.save()
    return render(request, 'gamesblog/game_detail.html', {'game_detail': game_detail, 'features':features, 'description':description, 'install_steps':install_steps, 'trendings':trendings[:10]})
