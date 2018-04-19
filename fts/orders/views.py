from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Order
from .utils.Utils import *

# Create your views here.

def index(request):
    all_orders = Order.objects.all()
    return render(request, 'orders/index.html', locals())


def new(request):
    if 'language' in request.POST and 'pages' in request.POST:
        order = Order()
#        token = request.POST['token']
        order.o_id = generate_id()
        order.lang = request.POST['language']
        order.pages = request.POST['pages']
        order.urgency = request.POST['urgency']
#        order.date = datetime.date.today().strftime("%d.%m.%Y")
#        order.file = request.POST['file']
        order.save()
        return JsonResponse({"response":"recd", "id":order.o_id})
    else:
        return JsonResponse({"response":"ferror"})


def test(request):
    d = enum(False)
    return HttpResponse(d)
