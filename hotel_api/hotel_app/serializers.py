from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Hotel, Review, Author, Favorite


class HotelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    date = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_date(obj):
        return obj.date.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'country', 'image', 'stars', 'date',
                  'description', 'price', 'likes', 'dislikes', 'user', 'location']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Review
        fields = ['id', 'message', 'created_at', 'likes', 'dislikes', 'positive', 'author']


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'
