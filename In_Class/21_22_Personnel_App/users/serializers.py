from rest_framework import serializers
from django.contrib.auth.models import User

# from .models import user
from rest_framework.validators import UniqueValidator 
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())] 
        )
    password=serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type" : "password"}
        )
    password2=serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type" : "password"}
        )
    class Meta:
        model=User
       
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
         ]
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"message" : "Password fields didn't match."})
        return data
    
    
    def create(self, validated_data):
        validated_data.pop('password2') #db de yok o yüzden çıkar
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password) # hash leme işlmi 
        user.save()

        return user
    
from dj_rest_auth.serializers import TokenSerializer
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","first_name","last_name","email")

class CustomTokenSerializer(TokenSerializer):
    
    user=UserTokenSerializer(read_only=True)
    
    class Meta(TokenSerializer.Meta):
        fields=("key","user")


#!1708 after models. Imagefield ugrastiktan sonra
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()   #!1808 09:31
    user_id=serializers.IntegerField(required=False)      #!1808 09:32  göndermek istiyorum , ama gerekli degil 

    class Meta:
        model = Profile
        fields = "__all__"

    #!1808 09:22 First// Modelserializers icindeki Updatei aldik. copy-paste 
    def update(self, instance, validated_data):
        instance=super().update(instance,validated_data)
        instance.user_id=self.context["request"].user.id        #!request yukarda false diyoruz burada manuel yapiyoruz. 
        instance.save()

        return instance


#!1708-- go to views.py