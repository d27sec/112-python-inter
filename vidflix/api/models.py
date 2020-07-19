from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from rental.models import Movie, Genre
from tastypie.authorization import Authorization
# Create your models here.

#resources to be exposed to the frontend 
#resources /api/???

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        ordering = ['id', 'name']
        filtering = {
            'id': ALL,
            'name': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions


class MovieResource(ModelResource):
    genre = fields.ToOneField(GenreResource, 'genre', full= True) # made the full = uppercase [T]rue

    class Meta:
        queryset =  Movie.objects.all()
        resource_name = 'movies'
        ordering = ['title','id', 'price', 'release_year']
        filtering = {
            'title' : ALL,
            'price' : ALL,
            'release_year' : ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions

