from django.contrib import admin
from . models import *

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderItem)