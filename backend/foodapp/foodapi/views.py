from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


class MealView(APIView):
    serializer_class = MealSerializer
    
    def get(self, request):
        output = [{'pk':output.pk ,"name": output.name,
                   "description": output.description, "price": output.price}
                   for output in Meal.objects.all()]
        return Response(output)