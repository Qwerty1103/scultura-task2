from django.http import HttpRequest
from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")