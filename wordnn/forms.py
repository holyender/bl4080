
from django import forms
 
class AddForm(forms.Form):
    word = forms.CharField()
    n = forms.IntegerField(initial=20)
    