from django import forms
from .models import ticket
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateTicketForm(forms.ModelForm):
    class Meta :
        model = ticket
        fields =['title','discription']


class UpdateTicketForm(forms.ModelForm):
    class Meta :
        model = ticket
        fields =['title','discription']


class ticket_detailsForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']