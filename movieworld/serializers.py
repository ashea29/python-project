from rest_framework import serializers
from .models import Director, Movie

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        view_name='movie_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Director
        fields = ('id', 'director_name', 'nationality', 'birthday', 'photo_url','bio',)

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    directors = serializers.HyperlinkedRelatedField(
        view_name='director_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ('id', 'director', 'name', 'genre', 'release_date','synopsis','photo_url',)
