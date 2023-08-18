
#! globalde Pagination olusturduk. localde olusturmak icin bu file i olusturduk.

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination

class MyNumberPagination(PageNumberPagination): #! PageNumberPagination i inherit ederek custom ediyorum.
    page_size = 10 
    page_query_param = "sayfa"                  #! default olarak querydeki(urls) key=page yerine . onun ismini sayfa olarak degistirdik.
    page_size_query_param = "adet"              #! http://127.0.0.1:8000/api/student/?adet=5 // queryi manuel olarak degistirerek page sayisini degistiriyoruz. 
    max_page_size = 3

class MyLimitPagination(LimitOffsetPagination):
    default_limit = 25                          #! sayfada 25 göster. http://127.0.0.1:8000/api/student/?limit=25&offset=25
    limit_query_param = "sinir"                 #! query de limit kelimesinin yerini alir.
    offset_query_param = "kacinci_veriden_itibaren"  #! query de offset kelimesinin yerini alir.

class MyCursorPagination(CursorPagination):
        ordering = "number"                     #! cursorpagination digerlerinden farkli olarak referans noktasi ister. default olarak created field ina bakar. ama suan benim verilerim arasdinda created olmadigi icin ordering ile kendim bir field tanimliyorum. numberi en kucuk olandan baslar. 
        page_size = 10 

