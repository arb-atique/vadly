from django.contrib import admin
from .models import Genre, Movies

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'daily_rate', 'number_in_stock')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)