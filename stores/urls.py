from stores.views import StoresViewSet, MyStoresViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', StoresViewSet, basename='stores')
router.register('my_stores/', MyStoresViewSet, basename='my_stores')
