from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "photo_number",
    )
    ordering = ["-pk"]


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
