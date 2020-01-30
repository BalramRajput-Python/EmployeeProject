from django import forms
from django.contrib.auth.models import User
from employee.models import Register

class Employee_Form(forms.ModelForm):

  class Meta:
    model = User
    fields = ['first_name','last_name','username','email','password','date_joined']

USER_ROLE00= [
    ('HR', 'HR'),
    ('Employee', 'Employee'),
    ]

class Employee_Form2(forms.ModelForm):
  
  user_type =forms.CharField(label="Role",widget=forms.Select(choices=USER_ROLE00))
  class Meta:
    model = Register
    fields = ['Qualification','WorkExp','user_type']