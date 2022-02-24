from django.db import models
from django.utils import timezone


class Movie(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    link = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)
    pubDate = models.DateField
    director = models.CharField(max_length=500)
    actor = models.CharField(max_length=500)
    userRating = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class SearchValue(models.Model):
    title = models.CharField(max_length=100)


class Review(models.Model):
    movie_info = models.ForeignKey('Movie', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review = models.CharField(max_length=5000)

    def __str__(self):
        return self.movie_info.title + "의 리뷰" +str(self.pk)