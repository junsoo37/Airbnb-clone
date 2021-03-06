from django.contrib import admin
from reservations import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished"
    )
