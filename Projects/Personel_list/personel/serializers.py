from rest_framework import serializers
from .models import Personel, Department



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = []


class PersonelSerializer(serializers.ModelSerializer):

    department= serializers.StringRelatedField()
    department_id=serializers.IntegerField()

    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()


    class Meta:
        model = Personel
        fields = (
            "id",
            "first_name",
            "last_name",
            "department",
            "department_id",
            "user",
            "user_id",
            "gender",
            "title",
            "salary",
            "started"
        )
