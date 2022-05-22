from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from calculator.models import Pizza
from calculator.serializers import PizzaSerializer


def calculate(request):
    return HttpResponse("Hello World - calculate")


def home(request):
    return HttpResponse("Hello World!")


def all_pizzas(request):
    pizzas = list(Pizza.objects.values())
    return JsonResponse(pizzas, safe=False)


@api_view(['GET'])
def pizza_list(request):
    pizzas = Pizza.objects.all()
    pizzas_serializer = PizzaSerializer(pizzas, many=True)
    return JsonResponse(pizzas_serializer.data, safe=False)
