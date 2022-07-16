from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from task3.models import Store
from task3.serializers import StoreSerializer


# Test data
# {
#     "name": "Store1",
#     "description": "Description1...description1...",
#     "rating": 10
# }
@api_view(http_method_names=['GET', 'POST'])
def stores(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer =StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)
