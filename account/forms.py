import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)





class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10, required=True, label="Ism")
    last_name = forms.CharField(max_length=10, required=True, label="Familiya")
    confirm = forms.CharField(max_length=10, required=True, label="Parolni qayta kiriting",
                              widget=forms.PasswordInput)


    def clean_first_name(self):
        data = str(self.cleaned_data.get('first_name'))
        if not re.match("^[A-Za-z]+$", data):
            raise ValidationError("Iltimos, faqat lotin harflarini kiriting")

        return data

    def clean(self):

        data = super().clean()

        if data.get('password') != data.get('confirm'):
            raise ValidationError({
                'confirm': 'Parollar bir xil emas'
            })

        return data

    class Meta:
        model = User
        widgets = {
            'password':forms.PasswordInput

        }
        labels = {
            'username': "Login",
            'password':"Parol",
            'first_name': 'Ism',
            'last_name': 'Familiya'
        }
        fields = ('username', 'password', 'confirm', 'first_name', 'last_name')

