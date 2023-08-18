from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"
        

class PostSerializers(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = "__all__"


