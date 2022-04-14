from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from rooms import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, per_page=10, orphans=5)

    try:
        rooms = paginator.page(page)
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")