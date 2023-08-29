from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"
        labels = {
            'first_name' : 'adinizi giriniz',
        }   #!2908  add de first name adinin yerini adinizi giriniz aliyor.
        widgets={
            'gender':forms.RadioSelect
        }