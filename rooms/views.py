from django.shortcuts import render
from rooms import models


def all_rooms(request):
    return render(request, "rooms/home.html", context={"rooms": models.Room.objects.all()})

