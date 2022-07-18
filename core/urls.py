from django.contrib import admin
from django.urls import path, include
from stores.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('task2/', include('task2.urls')),
    path('task3/', include('task3.urls')),
    path('stores/', include(router.urls))
]
