from rest_framework import serializers
from task3.models import Store


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=800)
    rating = serializers.IntegerField(min_value=1, max_value=100)

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store
