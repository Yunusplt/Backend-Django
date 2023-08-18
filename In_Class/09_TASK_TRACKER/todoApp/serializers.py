from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = "__all__"                     #todo hepsini istiyorum hepsi gelsin. tablodaki tüm fieldlar ve read only ler. 
        exclude = ["update_date"]               #todo update_date haric hepsi...
        # fields = ("task", "priority" )       #todo gelmesini istediklerimi yaziyorum. 