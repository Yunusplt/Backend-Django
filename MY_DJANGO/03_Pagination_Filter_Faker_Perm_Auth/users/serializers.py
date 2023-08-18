from rest_framework import serializers
from django.contrib.auth.models import User 
#! django yerlesik user model import ediyoruz. Normalde burada .model den model import ederdik 

#!KADIR HOCA ###############################################################################################

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]

    #override
    def validate(self, attrs):
        from django.contrib.auth.password_validation import validate_password      #! doğrulama fonksiyonu
        from django.contrib.auth.hashers import make_password                      #! şifreleme fonksiyonu
        password = attrs['password']            #! yukardakilerinin arasinda passwordu aldim. passworda atadim. 
        validate_password(password)
        # attrs["password"] = make_password(password)    #!!!!! querydict ler bu sekilde güncellenmez 
        attrs.update({
            "password": make_password(password)
        })
        return super().validate(attrs)
    
#!TOKEN
#?TOKEN
#!register isleminden sonra sifremi tokene dönustursun istiyorum. bunun icin override yapacam.
#!ModelSerializer a tikliyorum orginal kodlarina gidiyorum. orada MVS serializers a inherit etmis orayada tikliyorum 
#! ve asagidaki koda ulasiyorum . ilk bakista bos dönen bir method gibi gelse de. django burada bana su imkani sakliyor. 
#! api den dönen veriryi ben sana attrs icerisinde sunuyorum al ve overide et.
#?     def validate(self, attrs): 
#?        return attrs 
#?Bunlarin hepsi attrs icersiinde geliyor aslinda. 
        # {
        #    "id": 5,
        #     "password": "321",
        #     "is_superuser": false,
        #     "username": "fatih",
        #     "first_name": "fatih",
        #     "last_name": "fatih",
        #     "email": "fatih@gmail.com",
        #     "is_staff": false,
        #     "is_active": true
        # }
#!önemli bilgi... validate_password icinde hata raise ile firlatildigi icin. validate isleminde hata olursa islem devam etmez o yuzden if yapisina gerek yok. 
#! attrs querydict dir. farkli bir sekilde güncellenir. yukari bak...





#!SINAN HOCA ################################################################################################
# from rest_framework.validators import UniqueValidator
# class RegisterSerializer(serializers.ModelSerializer):
#     email=serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())]) #! emaili custom ediyoruz.
#     password = serializers.CharField(write_only=True, required=True)     #!password u da custom ediyoruz. veritabanindan kullaniciya gönderirken  tekrar bana göstermesini istemedigim icin write_only yaziyoruz
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields=(
#             'id',
#             'username',
#             'password',
#             'password2',
#             'first_name',
#             'last_name',
#             'email'
#             )
        
#     def validate(self, data):                           #!gelen data
#         if data['password']!=data['password2']:
#             raise serializers.ValidationError({"password":"didn't match"})
#         return data  

#     def create(self, validated_data):
#         validated_data.pop("password2")                 #! password2 dönen veriden cikartiliyor. tekrar görmenin anlami yok.
#         password = validated_data.pop("password")       #! password da dönen veriden cikartiliyor ama bu sefer password degiskenine kaydediyoruz.
#         user = User.objects.create(**validated_data)    #!
#         user.set_password(password)                     #! #hashliyor. sifreyi token gibi birseye döndürüyor.        
#         user.save()

#         return user      

# #todo serializer olusturduk views a geciyoruz. 

#!#############################################################################################################################################
