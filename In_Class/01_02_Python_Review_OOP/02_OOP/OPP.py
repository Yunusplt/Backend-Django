import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------")

#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class

#todo############################################################

#! Everything in Python is class
# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122, "henry", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test) 

#todo#############################################################

#! Defining class
#! Difference between class attributes and instance attributes

# class Person:
#      company = "clarusway"
#      department = "IT"

# person1=Person()        #? Person classindan person1 instance(nesne) i olusturuyoruz.
# person2=Person()

# print(person1.company)

#todo##########################################################

#! class'a attribute atama

# Person.job="developer"    #? Class a eklenen atrribute instancelarada otomatik gecer.
# print(person1.job)

#! instenca(nesne)ye attribute atama. hangisine atarsam ona ait olur. classtaki gibi hepsini kavramaz.
# person2.location="Germany"    #? instance e atanan attribute sadece o class a ait olur class i ve diger instanceleri(nesneleri) baglamaz.
# print(person2.location)

#todo##
#class Person:
#     company = "clarusway"
#     department = "IT"
    
#personA = Person()
#print(personA.city) #? instance önce kendine bakar bu attribute varmi? yoksa classina bakar. 
#personA.company="mercedes"
#print(personA.company) #? önce kendine bakti. burada var classa cikmiyor. 


#todo##########################################################

# #!self keyword 

# class Person:
#     company = "clarusway"
#     department = "IT"
    
#     def test(self):   #? class a function ekliyoruz. class a eklenen functionslara method denir.
#         print("test")
        
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     #! Static methods:
    
#     @staticmethod           #?decarator verirsek argument vermisiz gibi calisir. 
#     def salute():           #? static method ile cagirdigimiz zaman hangi nesne(instance) cagirirsa cagirsin farketmez oldugu gibi calisir. selften farkli
#         print("Hi there!")  #? yani cagirildigi nesneye göre sekil almaz static demek degismez demek.


# person1=Person()
# person2=Person()

# #print(person1.test())
# #Person.test(person1)  #? 85. satirdaki codeu. python aslinda arka planda bu sekilde calistiriyor. yani argument varmis gibi. bu yüzden yukarda def test i tanimladigimiz yerde argument veriyoruz. parantez icine self yaziyoruz. 

# person1.set_details("barry", 40)
# person2.set_details("henry", 35)

# person2.get_details()

# person1.salute()
# person2.salute()


#todo#######################################################

#! Special methods (init, str)   
#? pythonda tanimli ismi sabit ve belli görevi olan methodlardir.   
#! Encapsulation  & Abstraction
#? What is Encapsulation 
#? kullanicilarin bir classin attributelarina methodlarina ne kadar erisebilecigini ve ne kadarini degistirebileegini set ettigimiz kavram encupsltion .icerigi dillere göre degisebilir, Python da 100% bir enc. dan bahsedemeyiz. 
#!Abstraction (soyutlama) 
#? bir takim gereksiz bilgilerden kullaniciyi uzaklastirma. 
 
# class Person:
#     company = "clarusway"
#     department = "IT"

#     def __init__(self,name,age):  #? __ böyle baslayan methodlara doubleunderscore methodlar denir. dunder methods kisaltmasi 
#         self.name=name            #? ben bu Classtan instance üretince init otomatik calisacak. init cagirilan bir method degil yani. otomatik cagriliyor.  
#         self.age=age
#         self._salary=5000       #?(Encapsulation) degismesini istemiyorsam basina _ koyuyorum. ama bu sadece uyari asagida görülecegi gibi disaridan güncellenebiliyor. 
#         self.__id=35            #?(Encapsulation)

#     def __str__(self):
#         return f"{self.name} - {self.age}"
    
# person1 = Person("Hasan",40) 
# print(person1.name)
# print(person1)

# print(person1._salary)
# person1._salary = 4000
# print(person1._salary)              #? disardan ulasabiliyorum
# #print(person1.__id)                 #? disardan ulasamiyorum ve degistiremiyorum. 

# person1._Person__id = 23           #? bu sekilde degisip
# print(person1._Person__id)          #? bu sekilde ulasabilirim. 100% koruma yok Pythonda



# my_list = [3,4,1,5]               
# my_list.sort()                  #?sort methodunu kullanirken arkada calisan methodlari bilmiyorum. kullancii icin önemli degil Abstaction burada gerceklesiyor. soyutluyor kullanciyi arka plandan. 
# print(my_list)                  #? yani OOP kullancii geereksiz detaylardan uzaklastiriyor. bunlar oop nin güzel tarafi. 

#todo########################################################


#!  Inheritance  (Djangoda cok kullaniliyor ve önemli)
#? bir class olustururken baska bir classin özellikelrini kullanmak icin lazim 


class Person:
    company = "Clarusway"
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.age} created by __str__ method"
    
    def get_details(self):
        return print(self.name, self.age)

class Lang:
    def __init__(self, lang):
        self.lang = lang
        
    def display_langs(self):
        print(self.lang)


# class Employee(Person):   #?inheritance
#     pass

class Employee(Person, Lang):   #?multiple inheritance #? person ilk sirada ona super ile erisirken, lang ikinci sisrada ona kendi ismi ile erisiyorum.
    
    def __init__(self, name, age, path, lang, location="Germany"):
        super().__init__(name, age)      #? super keywordu inheritance yapilan classi ifade ediyor. parent classini temsil ediyor. parantte yoksa onun parantine cikiyor.
        # self.name = name               #? self.name ve self.age i artik super keywordu karsiliyor.
        # self.age = age
        self.path = path
        Lang.__init__(self, lang)
        # self.lang = lang
        self.location = location

    def get_details(self):          #? overriding parenttaki bir methodu alip kendimize göre yeniden custumise ettik.
        super().get_details()       #? burasi name ve age aliyor
        Lang.display_langs(self)
        print(self.path)
        print(self.location)
#? Employee classi önce kendi bünyesine bakiyor istenilen sey orada yoksa inharitance yapilan class a gidip oradan yazdiriyor.
#* Django da inheritance ve (Polymorphism (cok sekilcilik demek))overriding cok fazla yapicaz.
 
# emp1=Employee("victor",50)
# print(emp1)
# emp1.get_details() 

emp1 = Employee("victor", 33, ["fullstack", "devops"], ["python", "javascript"],"Turkey")
emp1.get_details()

emp1.display_langs()

#todo########################################################

print(Employee.mro())    #?(kalitim zinciri) Employee classi hangi classlardan inheritance edilerek olusturulmus onu görmek icin girdigimiz Befehl.
#*[<class '__main__.Employee'>, <class '__main__.Person'>, <class '__main__.Lang'>, <class 'object'>]

#print(help(Employee))    #? Employee class hakkinda detayli bilgi.
#?yukaridaki kodu calistirdiktan sonra code satirindan cikmak icin :Q 

#print(emp1.__dict__)      #? instance bazinda detaylari görmek.


#todo#########################################################

#? class icinde class innerclass...
# from django.db import models


# class Makale(models.Model):
#     adı = models.CharField(max_length=30)
#     yazarı = models.CharField(max_length=30)
    
#     class Meta:                  #?meta ismi static
#         ordering = ["yazarı"]


















print("-------------------------------------")


