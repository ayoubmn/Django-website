from django import forms
from  .models import ContactReception
class Cont(forms.ModelForm):
    class Meta :
        model = ContactReception
        fields =('nom','email','sujet','msg')


class Search(forms.ModelForm):
    class Meta :
        fields =('objet',)