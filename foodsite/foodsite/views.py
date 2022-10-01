from asyncio.windows_events import NULL
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from flask import jsonify

@csrf_exempt
def updateItem(request):
    global ids
    global qtys
    global cart
    cart = request.session['cart']
    if request.method == "POST":
        id = request.POST.get('iID')
        qty = request.POST.get('qty')

        global flag
        flag = 0
        for item in cart:
            if item.get('id') == id:
                flag = 1
                item.update({"qty": qty})
                request.session['cart'] = cart
        if flag == 0:
            data = {"id": id, "qty": qty}
            cart.append(data)
            request.session['cart'] = cart
        print(cart)
    return JsonResponse({"cart": cart})

@csrf_exempt
def homePage(request):
    cart = request.session['cart']
    if(request.method == "POST"):
        return JsonResponse({"cart": cart})
    return render(request,"index.html", {"cart": cart})

def reset(request):
    request.session['cart'] = []
    return redirect(homePage)
