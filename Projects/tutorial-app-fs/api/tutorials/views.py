from .serializers import TutorialSerializer, Tutorial
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class TutorialMVS(ModelViewSet):
    queryset = Tutorial.objects.all()         #! all yerine filter da kullanilabilir. statusü publish olanlari döndür gibi.response
    serializer_class = TutorialSerializer
