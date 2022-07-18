from django.contrib import admin
from django.urls import path, include
from stores.urls import router_stores, router_my_stores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('task2/', include('task2.urls')),
    path('task3/', include('task3.urls')),
    path('stores/', include(router_stores.urls)),
    path('my_stores/', include(router_my_stores.urls))
]
