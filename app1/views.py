from django.shortcuts import render

from app1.models import Vote


def votes(request):
    flavours = ['banana', 'chocolate', 'lemon']

    for flavour in flavours:
        Vote.objects.get_or_create(item=flavour)

    votes = Vote.objects.all()

    return render(request, "votes.html", {
        "votes": votes,
    })
