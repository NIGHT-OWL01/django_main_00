from django import forms
from django.forms import ModelForm
from playwithmodels.models import song,User

class songForm(ModelForm):
	class Meta:
		model=song
		fields='__all__'

class userForm(ModelForm):
	class Meta:
		model=User
		fields='__all__'