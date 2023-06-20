from django.urls import path
from . import views

urlpatterns = [
    path('', views.MealView.as_view(), name="MealView"),
]