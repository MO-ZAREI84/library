from django import forms 
class Person(forms.Form):
    name=forms.CharField(required=False)
    password=forms.CharField(max_length=25)