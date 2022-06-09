from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book

# Serializers define the API representation.
""" class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, validators=[function_name])
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
 """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'file')