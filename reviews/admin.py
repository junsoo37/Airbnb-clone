from django.contrib import admin
from reviews import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rating_average')
