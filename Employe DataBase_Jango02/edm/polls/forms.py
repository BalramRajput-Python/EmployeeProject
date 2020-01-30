from django import forms
from django.contrib.auth.models import User
from polls.models import Questions


class Question_Form(forms.ModelForm):

  ans = forms.CharField(label="Answer")
  question =  forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':50}))
  ch1 =  forms.CharField(label="Choice1")

  # created_by = forms.CharField(widget=froms.Texarea)

  class Meta:
    model = Questions
    fields = ['question','ch1','ch2','ch3','ans','created_by']
