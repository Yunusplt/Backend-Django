from rest_framework import serializers
from .models import (
    Category,
    Post,
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = "__all__"
        exclude =[]


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()       #! user: 1 seklinde idi bunu isme döndürdük-. Frontend isim görsün id degil
    user_id = serializers.IntegerField()          #! ama id yi de görmem lazim bunu yazdik 
    

    category = serializers.StringRelatedField()   #! category: 1 seklinde idi bunu isme döndürdük-.
    category_id = serializers.IntegerField()      #! ama id yi de görmem lazim bunu yazdik 



    class Meta:
        model = Post
        exclude = []