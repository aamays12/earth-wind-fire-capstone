from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	c = [("1", "Admin"), ("3", "Scheduler")]
	groups = forms.ChoiceField(choices=c, label="Groups")

	username = forms.CharField(
		label = ("Username"),
		help_text=(""),
	)
	
	password1 = forms.CharField(
		label = ("Password"),
		help_text=(""),
		widget=forms.PasswordInput,
	)
	password2 = forms.CharField(
        label=("Re-enter Password"),
        widget=forms.PasswordInput,
        
    )
	
	class Meta:
		model = User
		fields = ['groups', 'username', 'password1', 'password2', 'email']