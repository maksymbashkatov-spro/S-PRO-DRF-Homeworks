from django.urls import path
from task2.views import today, hello_world, my_name, calculator

urlpatterns = [
    path('today', today),
    path('hello_world', hello_world),
    path('my_name/', my_name),
    path('calculator/', calculator)
]
