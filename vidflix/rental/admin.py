from django.contrib import admin
from .models import Movie, Genre

#create template classes for the model
class MovieTemplate(admin.ModelAdmin):
    list_display = ('id', 'release_year', 'title', 'genre', 'price', 'in_stock')
    list_display_links = ('id', 'title')

    #fields = ('tile', 'release_year', 'genre', 'in_stock', 'image_url', 'length_min', 'date_created') # list of properties to ask when registering a new one
    exclude = ('price',)

class GenreTemplate(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links =('id','name')
# Register your models here.



admin.site.register(Movie, MovieTemplate)
admin.site.register(Genre, GenreTemplate)
