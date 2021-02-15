from rest_framework import serializers
from .models import Player, Clan

class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        exclude = []

class PlayerSerializer(serializers.ModelSerializer):

    clan = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Player
        exclude = ['password', 'user_permissions']

class PlayerInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = ['id', 'username', 'email', 'clan', 'coins', 'max_points']

class PlayerCreateSerializer(serializers.ModelSerializer):
    
    extra_kwargs = {'password': {'write_only': True}}
    class Meta:
        model = Player
        fields = ['id', 'username', 'email', 'coins', 'max_points', 'clan', 'password']

    def create(self,validated_data):
        player = Player(**validated_data)
        player.set_password(validated_data.get('password'))
        player.save()
        return player