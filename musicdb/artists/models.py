from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    song_list = models.ManyToManyField('songs.Song')

    def __str__(self):
        return "%s, id: %s" % (self.name, self.id)
