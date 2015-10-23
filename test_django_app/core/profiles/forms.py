from django import forms
from models import Profile
from parsley.decorators import parsleyfy


@parsleyfy
class ProfileCreationForm(forms.ModelForm):
	first_name = forms.CharField(label="first name", widget=forms.TextInput(attrs={'id':'first_name', 'class':'form-control', 'placeholder':'Slim'}))
	last_name = forms.CharField(label="last name", widget=forms.TextInput(attrs={'id':'last_name', 'class':'form-control', 'placeholder':'Shady'}))
	password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"id": "password", "class": "form-control", "placeholder": "Your password"}))
	username = forms.CharField(label="username", widget=forms.TextInput(attrs={'id':'last_name', 'class':'form-control', 'placeholder':'Shady123'}))
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'username', 'password', 'favorite_animal']


