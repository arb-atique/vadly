from django.db import models
from movies.models import Movies
from tastypie.resources import ModelResource

# Create your models here.
class MovieResources(ModelResource):
    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'    
        excludes = ['created_at']    
