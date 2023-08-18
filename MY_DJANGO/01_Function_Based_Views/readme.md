# Steps in installation of Django
- python -m venv env
- .\env\Scripts\activate     
- pip install djangorestframework            ( bu kod satiri ile hem Django hem restframework kurulur. Ayrica restframework documentation ziyaret edince göreceksin installed app e ekleme yapilmasini istiyor.)
- django-admin startproject main .
- pip install python-decouple    (.env icin) (bunu kurduktan sonra setting.py de SECRET_KEY i ayarla)   
- .env olustur
- .gitignore olustur
- python manage.py runserver
- python manage.py migrate       ( eger degisiklik olsaydi veya model olusturmus olsaydim once python manage.py makemigrations komutu yazilirdi.)
- python manage.py createsuperuser     (admine giris icin)
- pip freeze > requirements.txt        (sanal ortamda kullandigimiz paketler ve versionlarini requirements fileina kopyaliyoruz.)
- pip install -r .\requirements.txt    (repo dan proje cekersek böyle kuruyoruz.)
- python manage.py startapp firstApp
- python manage.py startapp appForModel (model icin app kurdum)
- appForModel.models.py dosyasinda modelini tanimla. 
- python manage.py makemigrations
- python manage.py migrate
- tanimladigin modeli admin panelde görmek icin ayni app klasörüünde admin.py dosyasina git modeli cagir ve admine ata.
- modelde resim var ise farkli bir yol izlenir. appForModels e bak.
- api olusturma step1: model.py / step2: serializers.py / step3: views.py  / step4: urls.py


