from django.db import models


# Create your models here.
class TMDB(models.Model):
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    vote_average = models.FloatField(null=True)
    description = models.TextField()
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title


