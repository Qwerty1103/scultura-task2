from asyncio.windows_events import NULL
from mimetypes import init
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect,render

def init(request):    
    request.session['ids'] = [0,0,0,0,0]
    request.session['qtys'] = [0,0,0,0,0]
    return redirect(homePage)

def homePage(request):
    return render(request,"index.html", {'qty': request.session['qtys']})

@csrf_exempt
def addItem(request):
    if request.method == "POST":
        if request.POST.get('iID') not in request.session['ids']:
            request.session['ids'][int(request.POST.get('iID'))] = request.POST.get('iID')
        if request.POST.get('iID') in request.session['ids']:
            request.session['qtys'][int(request.POST.get('iID'))] = int(request.POST.get('qty'))
    ids = request.session['ids']
    qtys = request.session['qtys']
    print(ids, qtys)
    return JsonResponse({'ids': ids, 'qtys': qtys})

@csrf_exempt
def removeItem(request):
    if request.method == "POST":
        if request.POST.get('iID') not in request.session['ids']:
            request.session['qtys'][int(request.POST.get('iID'))] = 0
        if int(request.session['qtys'][int(request.POST.get('iID'))]) > 0:
            request.session['qtys'][int(request.POST.get('iID'))] = int(request.session['qtys'][int(request.POST.get('iID'))]) - 1
        else:
            request.session['ids'][int(request.POST.get('iID'))] = 0
            request.session['qtys'][int(request.POST.get('iID'))] = 0
    ids = request.session['ids']
    qtys = request.session['qtys']
    print(ids, qtys)
    return JsonResponse({'ids': ids, 'qtys': qtys})