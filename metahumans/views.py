from django.shortcuts import render

from . import models #from .models import MetaHuamns, Team
                    #Si ponemos esto, no hace falta poner models. dentro de las clases

# Create your views here.

def list_all_metahumans (request):
    items = models.MetaHuman.objects.all()
    return render(request, "metahumans/list_metahumans.html", {
        "items": items,
    })


def list_all_teams (request):
    items = models.Team.objects.all()
    return render(request, "metahumans/list_teams.html", {
        "items": items,
    })

def detail_team(request, slug):
    team = models.Team.objects.get(slug=slug)
    return render(request, "metahumans/detail_team.html", {
        "team": team,
    })


def supermetahumans(request):
    items = models.MetaHuman.objects.exclude(level__lte=65).exclude(active=False)
    return render(request, "metahumans/list_supermetahumans.html", {
        "items": items,
    })






