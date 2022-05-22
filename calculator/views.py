from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from calculator.models import Pizza
from calculator.serializers import PizzaSerializer


def calculate(request):
    return HttpResponse("Hello World - calculate")


def home(request):
    return HttpResponse("Hello World!")


def all_pizzas(request):
    pizzas = list(Pizza.objects.values())
    return JsonResponse(pizzas, safe=False)


@api_view(['GET', 'POST'])
def pizza_list(request):
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        pizzas_serializer = PizzaSerializer(pizzas, many=True)
        return JsonResponse(pizzas_serializer.data, safe=False)
    if request.method == 'POST':
        pizza_data = JSONParser().parse(request)
        pizza_serializer = PizzaSerializer(data=pizza_data)
        if pizza_serializer.is_valid():
            pizza_serializer.save()
            return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
