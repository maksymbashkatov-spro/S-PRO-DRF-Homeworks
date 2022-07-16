from django.urls import path
from task3.views import stores

urlpatterns = [
    path('stores/', stores)
]
