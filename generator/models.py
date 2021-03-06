from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100, default=None, null=True)
    release_world = models.CharField(default=None, null=True, max_length=12)
    release_country = models.CharField(default=None, null=True, max_length=12)
    rating_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    rating_count = models.IntegerField(default=0, null=True)
    poster_url = models.CharField(max_length=1000, default=None, null=True)
    poster_alt = models.CharField(max_length=100, default=None, null=True)
    cover = models.CharField(max_length=1000, default=None, null=True)
    directors = models.TextField(default=None, null=True)
    countries = models.TextField(default=None, null=True)
    genres = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)
    movie_id = models.IntegerField(default=0, null=True)

class Series(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100, default=None, null=True)
    release_world = models.CharField(default=None, null=True, max_length=12)
    release_country = models.CharField(default=None, null=True, max_length=12)
    rating_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    rating_count = models.IntegerField(default=0, null=True)
    poster_url = models.CharField(max_length=1000, default=None, null=True)
    poster_alt = models.CharField(max_length=100, default=None, null=True)
    cover = models.CharField(max_length=1000, default=None, null=True)
    directors = models.TextField(default=None, null=True)
    countries = models.TextField(default=None, null=True)
    genres = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)
    series_id = models.IntegerField(default=0, null=True)

class Game(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100, default=None, null=True)
    release_world = models.CharField(default=None, null=True, max_length=12)
    release_country = models.CharField(default=None, null=True, max_length=12)
    rating_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    rating_count = models.IntegerField(default=0, null=True)
    poster_url = models.CharField(max_length=1000, default=None, null=True)
    poster_alt = models.CharField(max_length=100, default=None, null=True)
    cover = models.CharField(max_length=1000, default=None, null=True)
    developer = models.TextField(default=None, null=True)
    countries = models.TextField(default=None, null=True)
    genres = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)
    game_id = models.IntegerField(default=0, null=True)