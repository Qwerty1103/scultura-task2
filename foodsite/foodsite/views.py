from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def setCart(request):
    request.session['sname'] = ['1','2','3']
    return HttpResponse('Session')

def getCart(request):
    cartitems = request.session['sname']
    return HttpResponse(cartitems)