from rest_framework import serializers
from .models import User,Profile

class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = "__all__"

