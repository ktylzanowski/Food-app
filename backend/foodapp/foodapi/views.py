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
    
    def post(self, request):
        user_data = request.data.get('user')
        order_items = request.data.get('orderdItems')
        total = request.data.get('totalAmount')
        total = float(total[1:])
        order = Order.objects.create(name=user_data['name'],
                             street=user_data['street'],
                             city=user_data['city'],
                             postal=user_data['postal'],
                             total=total)
        order.save()
        for item in order_items:
            OrderItem.objects.create(order=order,
                                     meal=Meal.objects.get(name=item['name']),
                                     amount=item['amount'],).save()
            
        return Response()