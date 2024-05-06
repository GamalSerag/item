# imporrt WritableNestedModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from item.models import Item, MenuItemExtra, MenuItemExtraItem
from rest_framework import serializers

class MenuItemExtraItemSerializer(WritableNestedModelSerializer):
    class Meta:
        model = MenuItemExtraItem
        fields = ['id', 'name', 'price']

class MenuItemExtraSerializer(WritableNestedModelSerializer):
    items = MenuItemExtraItemSerializer(many=True)

    class Meta:
        model = MenuItemExtra
        fields = ['id', 'title', 'items']


class MenuItemSerializer(WritableNestedModelSerializer):
    extras = MenuItemExtraSerializer(many=True, required=True)


    class Meta:
        model = Item
        fields = ['id', 'name', 'image_url', 'extras']