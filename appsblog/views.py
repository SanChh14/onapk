from django.shortcuts import render, get_object_or_404
from .models import Appsblog
from gamesblog.models import Gamesblog
from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def appsblog(request):
    games = Gamesblog.objects.all()
    apps = Appsblog.objects.all().order_by('-pub_date')

    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)

    paginator = Paginator(apps, 5)
    page = request.GET.get('page')
    apps = paginator.get_page(page)

    return render(request, 'appsblog/appsblog.html', {'apps': apps,'trendings':trendings[:10]})

def app_detail(request, appsblog_id):
    apps= Appsblog.objects.all()
    games = Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    app_detail = get_object_or_404(Appsblog, pk=appsblog_id)
    features= list(app_detail.features.split('\n'))
    install_steps= list(app_detail.install_steps.split('\n'))
    description = list(app_detail.description.split('\n'))
    app_detail.views = app_detail.views+1
    app_detail.save()
    return render(request, 'appsblog/app_detail.html', {'app_detail': app_detail, 'features':features, 'description':description, 'install_steps':install_steps, 'trendings':trendings[:10]})
