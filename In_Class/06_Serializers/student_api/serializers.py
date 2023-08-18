
#todo #### view ve url ayarladiktan sonra bu file i olusturduk. 1
from rest_framework import serializers  
#todo model kullanacaz import et.
from .models import Student, Path 

"""Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.  """


# class StudentSerializer(serializers.Serializer):             #todo ilkel kisim biz bunu kullanmayacagiz asagidaki kisimi kullanacaz.
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    # number = serializers.IntegerField(required=False)
    # age = serializers.IntegerField()


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):  #todo StudentSerializer osman da olabilir.  model serializer
    
    born_year = serializers.SerializerMethodField() #!read only   #todo yeni bir data field ekleme   1
    path=serializers.StringRelatedField()   #!read only #todo path field sadece id dönmesin front ent anlasin diye isim degistiriyourz.
    path_id=serializers.IntegerField()      #!frontend gönderirken yazabilmem icin ekliyorum.

    class Meta:                         #todo meta class i innerclasstir. o modelle ilgili ayarlar yapmamizi sagliyor. s
        model = Student
        fields = "__all__"
        #fields = ("first_name","age")  #todo isim ve age istiyorum. get istegi atinca sadece bunlar dönecek.....
        # exclude = ["number"]          #todo number haric digerlerini getirir. 

    def get_born_year(self,obj):                       #todo yeni bir data ekleme  2   function ismi böyle olmak zorunda.
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    

class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]    #todo ## buraya student ekledigim zaman get api yapinca studentleri id nolari ile görüyorum. student hakkinda tüm bilgilere ulasmak icin 48. satirdaki kodu yaziyorum. students leri yeniden tanimliyorum.

        