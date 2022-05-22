from rest_framework import serializers
from calculator.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'type',
            'published_date',
            'size',
            'hydro',
        )
