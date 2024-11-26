from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

import datetime


def register_login_page(request, clicked="login"):
    if request.method=="POST":
        next_page = request.GET.get('next')
        if "register" in request.POST:
            form_register = UserCreationForm(request.POST, auto_id="register_%s")
            if form_register.is_valid():
                form_register.save()
                username = form_register.cleaned_data.get('username')
                login(request, User.objects.get(username=username))
                messages.add_message(request, messages.SUCCESS, f'Account created for {username}.')
                if next_page == None:
                    return redirect(reverse('home'))
                return redirect(reverse(next_page))
            else:
                for field, errors in form_register.errors.items():
                    for error in errors:
                        messages.add_message(request, messages.ERROR, f'{error}')
        elif "login" in request.POST:
            form_login = AuthenticationForm(data=request.POST, auto_id="login_%s")
            if form_login.is_valid():
                user = form_login.get_user()
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'You have been logged in.')
                if next_page == None:
                    return redirect(reverse('home'))
                return redirect(reverse(next_page))
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password. Please try again.')

    form_register = UserCreationForm(auto_id="register_%s")
    form_login = AuthenticationForm(auto_id="login_%s")
    context={
        "form_register":form_register,
        "form_login":form_login,
        "clicked":clicked,
    }
    return render(request, "registration/register_login.html", context)


def logout_view(request):
    response = redirect(reverse('home'))
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
    else:
        messages.add_message(request, messages.ERROR, 'You are not logged in.')
    return response


def home(request):
    return render(request, 'home.html')


def wip(request):
    return render(request, 'wip.html')