from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Hotel, Review, Author


class HotelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'country', 'image', 'stars',
                  'description', 'price', 'likes', 'dislikes']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Review
        fields = ['id', 'message', 'created_at', 'likes', 'dislikes', 'positive', 'author']






