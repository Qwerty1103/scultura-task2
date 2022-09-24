from asyncio.windows_events import NULL
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect,render

def homePage(request):
    return render(request,"index.html")

@csrf_exempt
def addItem(request):
    if request.method == "GET":  
        request.session['ids'] = 0
        request.session['qtys'] = 0
    elif request.method == "POST":
        request.session['ids'] = request.POST.get('iID')
        request.session['qtys'] = request.session['qtys'] + 1
    ids = request.session['ids']
    qtys = request.session['qtys']
    return JsonResponse({'ids': ids, 'qtys': qtys})