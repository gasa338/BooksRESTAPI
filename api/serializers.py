from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'alt', 'src']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'image']


class GenreSerializerDetail(serializers.ModelSerializer):
    image = ImageSerializer(many=False)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'image']


class WriterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'date_of_birth', 'date_of_death', 'genre', 'about_them']


class WriterSerializerDetail(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'date_of_birth', 'date_of_death', 'genre', 'about_them']


class WriterSerializerCreate(serializers.ModelSerializer):
    # genre = GenreSerializer(many=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'date_of_birth', 'date_of_death', 'genre', 'about_them']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'about_them']


class BookSerializerCreate(serializers.ModelSerializer):
    genre = GenreSerializer(many=True).data
    writer = WriterSerializer(many=False).data
    publisher = PublisherSerializer(many=False).data
    image = ImageSerializer(many=False).data

    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'number_of_page', 'writer', 'publisher', 'publish_data', 'description',
                  'price', 'quantity', 'image']


class BookSerializerList(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    writer = WriterSerializer(many=True)
    publisher = PublisherSerializer(many=False)
    image = ImageSerializer(many=False)

    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'number_of_page', 'writer', 'publisher', 'publish_data', 'description',
                  'price', 'quantity', 'no_of_ratings', 'avg_rating', 'image']


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name']


class ReviewSerializerDetail(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    book = BookSimpleSerializer(many=False)

    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'comment', 'rating', 'approved']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_id = instance.user_id
        try:
            profile_obj = Profile.objects.get(user=user_id)
            image_data = Image.objects.get(pk=profile_obj.image_id)
            data['user_image'] = ImageSerializer(image_data).data
        except:
            data['user_image'] = None
        return data


class ReviewSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id']


class ReviewSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'comment', 'rating']

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['user_id'] = UserSerializer(instance.user).data.get('id')
    #     return data


class ProfileSerializer(serializers.ModelSerializer):
    # image = ImageSerializer(many=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'about', 'genre', 'image']


class ProfileSerializerDetail(serializers.ModelSerializer):
    image = ImageSerializer(many=False)
    genre = GenreSerializer(many=True)
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'about', 'genre', 'image']


class ReservationSerializer(serializers.ModelSerializer):
    books = BookSimpleSerializer(many=False)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'books', 'datetime', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'books', 'quantity', 'status']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CartListSerializer(serializers.ModelSerializer):
    books = BookSimpleSerializer(many=False)
    user = UserListSerializer(many=False)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'books', 'quantity', 'status']
