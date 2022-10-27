from django import forms
from .models import (
    Stream,
    Student
)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','second_name','adm_no','age','mystream']
       