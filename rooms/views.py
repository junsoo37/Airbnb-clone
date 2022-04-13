from math import ceil
from django.shortcuts import render
from rooms import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    offset = page_size*(page-1)
    limit = offset+page_size

    rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
          }
    )

