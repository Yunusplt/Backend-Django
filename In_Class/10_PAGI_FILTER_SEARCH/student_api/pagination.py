
#! setting.py daki page ayarlamasinii burada yapacaz.
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyNumberPagination(PageNumberPagination):
    page_size=5                                  #! apide 1 sayfada gözüken veri sayisi
    page_query_param="seite"                     #! querydeki key=page yerine
    page_size_query_param="adet"                 #! 6.satirdakinin endpoindli hali.
    # max_page_size=3

class MyLimitPagination(LimitOffsetPagination):
    default_limit=8
    limit_query_param="kac_tane"
    offset_query_param="kacinci"

class MyCursorPagination(CursorPagination):
    page_size = 10
    ordering = "number"                          #! number a göre siralama yapti.
