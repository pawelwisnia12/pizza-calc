from django.http import HttpResponse, JsonResponse

from calculator.models import Pizza


def calculate(request):
    return HttpResponse("Hello World - calculate")


def home(request):
    return HttpResponse("Hello World!")


def all_pizzas(request):
    pizzas = list(Pizza.objects.values())
    return JsonResponse(pizzas, safe=False)
