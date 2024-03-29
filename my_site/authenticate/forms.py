from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
   
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
        def __init__(self, *args,**kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            
            self.fields['username'].widget=forms.TextInput(attrs={"class": "form-control"})
            self.fields['password1'].widget=forms.TextInput(attrs={"class": "form-control"})
            self.fields['password2'].widget=forms.TextInput(attrs={"class": "form-control"})