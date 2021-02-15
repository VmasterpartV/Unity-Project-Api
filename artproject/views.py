from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PlayerSerializer, ClanSerializer, PlayerInfoSerializer, PlayerCreateSerializer
from .models import Player, Clan

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    filterset_fields = []
    search_fields = ['username', 'email']
    ordering_fileds = ['id', 'username', 'coins', 'max_points']
    ordering = ['-date_joined']

    def get_queryset(self):
        clan = self.request.user.clan
        return Player.objects.filter(clan=clan)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlayerInfoSerializer
        if self.action == 'create':
            return PlayerCreateSerializer
        return PlayerSerializer

class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer