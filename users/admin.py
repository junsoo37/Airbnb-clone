from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar", "gender", "bio", "birthdate", "language", "currency", "superhost"
                )
            }
        ),
    )