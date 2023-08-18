### Testing in Django Rest Framework
- tests.py mevcut. o varken tests Folderi(yapcagim testler fazla ise cesitli ise folder icinde filelar olusturuyorum) acarsam. tests.py silmek zorundayim. iki ayni isim test olamaz!!!! 
- in Terminal 
-  1 pip install coverage
-  2 coverage run --omit='*/env/*' manage.py test
-  3 coverage report
-  4 coverage html
- sol tarafta htmlcov folderi aciliyor. onun icerisinde index.html sag tik open with live server diyouruz. orada coveragelerin hepsini browserde görebiliyoruz.
- python manage.py test    birkez coverage run dedikten sonra bu komutlada test baslatabiliriz.
- amac %60 - 80 olanlari %100 yapmak...



- in flights tests.py


- coverage run manage.py test           en son yeniden bu