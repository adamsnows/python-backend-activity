from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get_queryset(self):
        album_id = self.kwargs[self.lookup_field]
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs[self.lookup_field]
        album = get_object_or_404(
            Album,
            pk=album_id,
        )
        serializer.save(album=album)
