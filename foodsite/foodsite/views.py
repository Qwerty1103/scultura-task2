from asyncio.windows_events import NULL
from mimetypes import init
import re
from turtle import home
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect,render

id = [-1,-1,-1,-1,-1]
qty = [0,0,0,0,0]

def homePage(request, ids, qtys):
    return render(request,"index.html", {'id': ids, 'qty': qtys})

@csrf_exempt
def updateItem(request):
    global id
    global qty
    if request.method == "POST":
        if id[int(request.POST.get('iID'))] != int(request.POST.get('iID')):
            id[int(request.POST.get('iID'))] = int(request.POST.get('iID'))
        if id[int(request.POST.get('iID'))] == int(request.POST.get('iID')):
            qty[int(request.POST.get('iID'))] = int(request.POST.get('qty'))
        if qty[int(request.POST.get('iID'))] == 0:
            id[int(request.POST.get('iID'))] = -1
        print(id,qty)
        return JsonResponse({'ids': id, 'qtys': qty})
    if request.method == "GET": 
        return init(request, id, qty)

def init(request, id, qty):
    print(id,qty)
    return homePage(request, id, qty)