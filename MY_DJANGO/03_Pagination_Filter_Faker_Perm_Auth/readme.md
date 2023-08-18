## Steps
- pull edildiginde student_api ve icerisinde models.py serializers.py  views.py  urls.py  mevcuttu.

### FAKER
- Pagination olusturmak icin cok fazla veriye ihtiyacim var onun icin Faker kullaniyoruz. 
- create a faker.py file. file olusturduktan sonra hocadan copy-paste komutlar orada yaziyor.

### PAGINATION
- https://www.django-rest-framework.org/api-guide/pagination/  e git komutlari takip et. 
- main.settings.py  rest_frame work e bak  3 farkli pagination var 
- first : PageNumberPagination
- farkli modellerin farkli pagination a sahip olmasi icin pagination.py file i olusturduk. cünkü setting.py daki globaldir.
- second : LimitOffsetPagination   
- globalde(main.settings.py) ve localde(student_api.pagination.py) tanimliyoruz.
- third : CursorPagination
- Hata aldik digerlerinden farkli ne ? =>> CursorPagination referans noktasi ister. ordering ile referans belirliyoruz.

### FILTER
- ilk önce manuel filter yaptik.  in views.py
- install ederek filter.  pip install django-filter
- installed app lere ekle. settigs.py git REST_FRAMEWORK Icine ekle 
- views.py e git  filterset_fields=['first_name',]  bunu yaz
- bundan sonra Browsable api de filter butonu cikacak 
- local kullanimi yapildi.   filter_backends = [DjangoFilterBackend]
- filterset_fields = tam ismi yaz. 
- search_fields = ar yaz ve isminde ar olan tüm isimleri filtrelesin 
- ordering_fields = belirledigimiz field e göre artan azalan seklinde listelenir. 



### PERMISSION - AUTHENTICATION - TOKEN
- REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated',]} documantaion dan al ve setting.py e ekle. 
- localde de tanimladik student modeli icin. 
- Basic Authentication ile olusturulmus sifre base64 decoder da cözülebiliyor. 
- Permission gibi documentaion dan aldik. setting.py de 

- Token Auth..   'rest_framework.authtoken'   installed apslere ekle. install yapmadan. 
- python manage.py migrate   yap. bunu yapinca authtoken_token gelir db ye. 
- setting.py a documentaiondan global tokenauthentication aata. 
- 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
- bu islemlerden sonra admin panelde AUTH TOKEN alani olustu. 


- users appi olusturuldu.
- users icin model olusturmuyoruz. Djangonun yerlesik useri ni kullaniyoruz. 
- urls.py / serializers.py / 
- users/register in postmann
  body : {
    "email": "veli@gmail.com",
    "password" : "321",
    "password2" : "321",
    "username" : "veli",
    "first_name" : "veli",
    "last_name" : "veli"
}

- dönen veri: {
    "message": "created successfully",
    "details": {
        "id": 3,
        "username": "veli",
        "first_name": "veli",
        "last_name": "veli",
        "email": "veli@gmail.com",
        "token": "ce4411d1f66bd6ed6226a52bbed929fc62e5911f"
    }
}



