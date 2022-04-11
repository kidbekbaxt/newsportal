import re
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _


def account_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:

                login(request, user)

                messages.success(request,f"{user.get_full_name()} Xush kelibsiz!")
                return redirect('main_index')




        form.add_error('password', _("Login va/yoki parol noto'g'ri"))

    return render(request, 'account/login.html', {
        'form': form
    })



def account_registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():

            form.instance.set_password(form.cleaned_data.get('password'))
            form.save()

            messages.success(request, 'Siz ro`yxatdan o`tdingiz!!! ')

            return redirect('main_index');

    return render(request, 'account/registration.html', {
        'form': form
    })

def account_logout(request):
    messages.success(request, f"Kelib turing {request.user.get_full_name()}!!")
    logout(request)

    return redirect('main_index')