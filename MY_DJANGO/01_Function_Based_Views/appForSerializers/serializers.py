
#!step:2
from rest_framework import serializers  
from .models import Student2,Path

"""Serializers allow complex data such as querysets and model instances to be converted to native
 Python datatypes that can then be easily rendered into JSON, XML or other content types. 
 Serializers also provide deserialization, allowing parsed data to be converted back into complex types, 
 after first validating the incoming data.  """


#? Way-1 : ilkel yol
# class StudentSerializers(serializers.Serializer):           #todo model.py daki student modelini oldugu gibi burada tekrar yaz
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student2.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name=validated_data.get("first_name", instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

#? Way-2 : bizim calisacagimiz yol

class Student2Serializer(serializers.ModelSerializer):
    born_year = serializers.SerializerMethodField()   #!read only 
    path = serializers.StringRelatedField()           #!read only  #frontend'de sadece id dönmesin kullanici anlasin diye bu yöntem
    path_id = serializers.IntegerField()              #! backend'de buradan anlasin diye path_id

    class Meta:                         #todo Meta Class innner classdir. modelle ilgili ayarlar yapmamizi saglar.
        model = Student2
        fields = "__all__"
        #fields = ("first_name", "age") #todo get istegi atinca dönmesini istedigim fieldlari belirliyorum
        #exclude = ["number"]           #todo number haric digerlerini döndür.

    def get_born_year(self,obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    

class PathSerializer(serializers.ModelSerializer):

    students = Student2Serializer(many=True, read_only=True)

    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]   #todo buraya student ekledigim zaman get api yapinca studentleri id nolari ile görüyorum. student hakkinda tüm bilgilere ulasmak icin 51. satirdaki kodu yaziyorum. students leri yeniden tanimliyorum.










