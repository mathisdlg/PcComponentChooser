from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def wip(request):
    return render(request, 'wip.html')