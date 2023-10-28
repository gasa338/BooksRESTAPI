from rest_framework import serializers
from api.models import *
from rest_framework.authtoken.models import Token


class GenreSerializerHelpers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class WriterSerializerHelpers(serializers.ModelSerializer):
    genre = GenreSerializerHelpers(many=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'date_of_birth', 'date_of_death', 'genre']


class GenreSerializerPostHelpers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id']


class WriterSerializerPostHelpers(serializers.ModelSerializer):
    genre = GenreSerializerHelpers(many=True)

    class Meta:
        model = Writer
        fields = ['id']


class PublisherSerializerHelpers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']