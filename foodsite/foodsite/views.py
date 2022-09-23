from asyncio.windows_events import NULL
from contextlib import nullcontext
import string
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect,render

def homePage(request, ids = 0, qtys = 0):
    return render(request,"index.html", {'ids': ids, 'qtys': qtys})

@csrf_exempt
def setCart(request):
    if request.method == "POST":
        request.session['ids'] = request.POST.get('iID')
        request.session['qtys'] = request.POST.get('qty')
    return getCart(request)

def getCart(request):
    ids = request.session['ids']
    qtys = request.session['qtys']
    ids = 1
    qtys = 1
    return redirect('/', ids, qtys)