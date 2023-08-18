#
#! serializers i import ederek basliyoruz..

from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField()  # read_only
    path_id = serializers.IntegerField()

    class Meta:
        model = Student
        fields = "__all__"
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    

class PathSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]



#todo- fields in farkli kullanimlari. 
#? exclude = []  bu da all a esittir. 
#? exclude = [ dahil etmeyi istemedigimiz field i buraya yaziyoruz]

#todo- 