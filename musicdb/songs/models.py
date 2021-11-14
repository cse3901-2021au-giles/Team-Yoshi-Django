from django.db import models

import random

# generate random time length
def random_length(): 
    mins = random.randrange(3) + 1
    seconds = random.randrange(60)
    if seconds < 10:
        seconds = "0%s" % seconds
    time = "0%s.%s" % (mins, seconds)
    return time

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist_obj = models.ForeignKey("artists.Artist", on_delete=models.CASCADE) 
    length = models.CharField(max_length=10, default=random_length(), editable=False)
    
    # Method to print formatted string
    def __str__(self):
        return "%s, id: %s" % (self.name, self.id)
