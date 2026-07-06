from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    ordering = ['title']

admin.site.register(Movie, MovieAdmin)
