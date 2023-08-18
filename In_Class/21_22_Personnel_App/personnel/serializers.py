
#!1808  10:44

from rest_framework import serializers
from .models import Department,Personnel

#! 1808 11:02 alternatif olarak FixModel ekledik buraya. temiz kod icin

class DepartmentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()                      #!1808 11:00 after admin:panel user:1 gördükten sonra 
    user_id=serializers.IntegerField(required=False)            #!1808 11:00 after admin:panel user:1 gördükten sonra 

    personnels=serializers.StringRelatedField(many=True)    #!1808 12:33  Departmani cagirdigimizda hangi userlar bu departmanda görmek icin 
    personnel_count=serializers.SerializerMethodField()      #!1808  11:11   Method fieldlar sadce read only dir. 
    class Meta:
        model = Department
        # fields = "__all__"
        fields = ("id", "name","personnels","personnel_count")
    
    #!1808 11:07 method field kullanacaksam get ile baslamali. Bu departmanda calisan personellerin sayisina ulasmak istiyoruz.
    #! Department dan Personnel e nasil ulasabilirim. go to models add related_name  
    def get_personnel_count(self,obj):
        return obj.personnels.count()     #! related_name ile bunun uyusmasi lazim. 


from django.utils.timezone import now   #!1108 11:35
class PersonnelSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()                       #!1808 11:00 after admin:panel user:1 gördükten sonra 
    user_id=serializers.IntegerField(required=False)            #!1808 11:00 after admin:panel user:1 gördükten sonra 


    days_since_started=serializers.SerializerMethodField()   #!1108 11:35
    class Meta:
        model = Personnel
        fields = "__all__"
    
    #!1108 11:35 after 2.pause
    def get_days_since_started(self,obj):

        return (now()-obj.start_date).days                  #!1108  11:46 go to admin panel.

#!1808  10:47 go to views.py 