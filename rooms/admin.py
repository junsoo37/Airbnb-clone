from django.contrib import admin
from rooms import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition"""
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("amenities", "facilities", "house_rules")}),
        ("More About the Space", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("hosts",)})
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities"
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "hosts__superhost",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    # if you want to using foreign key as search fields use "{foreignkey}__{field_name}"
    search_fields = ("city", "hosts__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules"
    )

    # obj는 해당 row (즉 Room Row), self는 admin
    def count_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition"""
    pass
