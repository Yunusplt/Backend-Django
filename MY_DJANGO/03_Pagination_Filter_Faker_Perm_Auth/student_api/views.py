from django.http.response import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import Student, StudentSerializer, Path, PathSerializer
#!PAGINATION 
from .pagination import MyNumberPagination, MyLimitPagination, MyCursorPagination
#!FILTER.    globali kapattik, localde tanimliyacagiz
from django_filters.rest_framework import DjangoFilterBackend   #! globaldakinin köseli parantezine benziyor.
from rest_framework.filters import SearchFilter, OrderingFilter                #! 2. filter tarzi
#! PERMISSION 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #!PERMISSION 
    # permission_classes = [IsAuthenticated]                  #! Student modelinde permission atadik pathde yok. login ise apiye ulasir. 
    # permission_classes = [IsAuthenticatedOrReadOnly]        #! login degilse sadece okusun. 
    permission_classes = [IsAdminUser]                        #! sadece admin olanlar erissin 

    #!PAGINATION
    pagination_class = MyNumberPagination                #! custom edilmis pagination kullaniliyor. from pagination.py. 
    # pagination_class = MyLimitPagination               #! custom edilmis LimitOfsetPagination. from pagination.py.
    # pagination_class = MyCursorPagination

    #!FILTRE  manuel olarak olusturduk. daha sonrada instal filter ile olusturduk. bu manuel olan. 
    # def get_queryset(self):
    #     queryset = Student.objects.all()
    #     path = self.request.query_params.get('path')        #! path osman da olabilir. 
    #     if path:
    #         my_path = Path.objects.get(path_name=path)
    #         queryset = queryset.filter(path=my_path.id)
    #     return queryset
    #!FILTRE with install filter.
    filterset_fields=['first_name',]          #! filter install edildikten sonra bunu yaz... globaldeki ile birlikte bunu yazmistik.
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]   #! localde import ettikten sonra bunu yaz...
    search_fields = ['first_name']
    ordering_fields = ['number', ]                                    #! number a göre artan veya azalan sirada listeleyebiliriz. artan mi azalanmi Browserdan secilir. 
    #! filterset_field da tam ismi yazmak gerekirken "arzu"
    #! search_fields da "ar" yazarsak icerisinde ar gecen tüm isimleri getirir.

class PathMVS(ModelViewSet):                   #! globalden gelen pagination uygulaniyor burada 2 veri gözükür sayfada....
    queryset= Path.objects.all()
    serializer_class = PathSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["path_name",]