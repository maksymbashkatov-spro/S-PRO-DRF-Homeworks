from stores.views import StoresViewSet, MyStoresViewSet
from rest_framework import routers


router_stores = routers.SimpleRouter()
router_stores.register('', StoresViewSet, basename='stores')

router_my_stores = routers.SimpleRouter()
router_my_stores.register('', MyStoresViewSet, basename='my_stores')
