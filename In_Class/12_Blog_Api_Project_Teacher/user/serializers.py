from rest_framework import serializers
from django.contrib.auth.models import User
#!django yerlesik user model kullaniyoruz.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]

    #override
    def validate(self, attrs):
        
        from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
        from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
        password = attrs["password"]     #!passwordü aldik... 
        validate_password(password)      #!passwordü validate soktuk.
        # attrs["password"] = make_password(password)    #!!!!! querydict ler bu sekilde güncellenmez 
        attrs.update({
            "password": make_password(password)
        })
        return super().validate(attrs)