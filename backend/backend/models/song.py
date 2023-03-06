from django.db import models

class Song(models.Model):
    url = models.CharField(max_length=150, blank=False, null=False, primary_key= True)
    title = models.CharField(max_length=100, blank=False, null=False)
    artist = models.CharField(max_length=100, blank=False, null=False)
    source = models.CharField(max_length=100, blank=False)
