from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from task3.models import Store
from stores.serializers import StoreSerializer


# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# u = User.objects.all()
# t = Token.objects.all()
#
# user = User.objects.create_user(username='User1', password='User1User1')
# token = Token.objects.create(user=user)
# Authorization: Token 97e0b0b53ab3384daae7a10b49863fc53883ab83
class StoresViewSet(ModelViewSet, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})


class MyStoresViewSet(ModelViewSet, GenericViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Store.objects.filter(owner=self.request.user)
