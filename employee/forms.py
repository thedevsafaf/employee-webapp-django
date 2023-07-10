from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ("emp_name","emp_email","emp_phone","emp_role","emp_salary")

        widgets = {
            'emp_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'emp_email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'emp_phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'emp_role' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Role'}),
            'emp_salary' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Salary'}),
        }
