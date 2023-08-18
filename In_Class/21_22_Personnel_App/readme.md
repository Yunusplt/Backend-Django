<!-- 
- eger gömülü user yerine kendim user model olusturup kullanacaksam. 
- 1- tanimladigim modeli settings.py da tanimlamam lazim  / AUTH_USER_MODEL = 'users.MyUser'
- 2- admin.py da code blogu.

- models.py create Profile model in users/models.py
- for Image
--- pip install Pillow
--- go to settings.py
--- go to main/urls.py
- serializers.py    modelimiz hazir, serializera gidiyoruz..   create ProfileSerializer
- views.py          serializer hazir, views e gidiyoruz...     update ProfileUpdateView 
--- user olustugunda o usera a ait otomatik Profile olussun istiyoruz. therefore it is not create  
- urls.py           path("profile/<int:pk>", ProfileUpdateView.as_view())


$$ 1708    2:35:00
 -->