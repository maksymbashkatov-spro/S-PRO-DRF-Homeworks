from stores.views import StoresViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', StoresViewSet, basename='stores')
