from django.shortcuts import render
from rest_framework import generics

from item.models import Item
from item.serializers import MenuItemSerializer

# Create your views here.
class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = MenuItemSerializer