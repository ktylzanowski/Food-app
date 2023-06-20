from rest_framework import serializers
from . models import *

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ['pk', 'name', 'description', 'price']