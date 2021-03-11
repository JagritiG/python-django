from django.contrib import admin
from .models import TMDB


# Register your models here.
@admin.register(TMDB)
class TMDBAdmin(admin.ModelAdmin):
    pass
