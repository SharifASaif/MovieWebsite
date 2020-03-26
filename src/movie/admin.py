from django.contrib import admin

# Register your models here.
from .models import Movie , Movielink







admin.site.register(Movie)
admin.site.register(Movielink)