from rest_framework import serializers
from task3.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'rating', 'owner', 'status')
