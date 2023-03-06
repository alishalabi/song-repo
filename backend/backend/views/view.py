from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.models.song import Song
from backend.serializers.songs_serializers import SongSerializer

class SongList(APIView):
    """
    List all song, or create a new song.
    """

    def get(self, request, format=None):
        """
        Return a list of all songs.
        """
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a song.
        """
        serializer = SongSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):
    """
    Retrieve, update, or delete a song.
    """

    def get(self, request, pk, format=None):
        song = Song.objects.get(url=pk)
        serializer = SongSerializer(song, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        song = Song.objects.get(id=pk)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = Song.objects.get(id=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
