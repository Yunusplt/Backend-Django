
#! appForSerializers dan kopyalandi.
from rest_framework import serializers
from .models import Student, Path

class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()    # read_only
    path = serializers.StringRelatedField()            # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ("first_name", "age" )
        # exclude = ['number']
        
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age


class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]