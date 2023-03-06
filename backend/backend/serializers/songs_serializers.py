from rest_framework import serializers
from api.models.song import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        song = Song
        fields = ['url', 'title', 'artist', 'source']
