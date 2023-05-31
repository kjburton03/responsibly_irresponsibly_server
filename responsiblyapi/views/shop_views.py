# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from responsiblyapi.models import Shop, Client
# from django.contrib.auth.models import User

class ShopView(ViewSet):

    def retrieve(self, request, pk):
        """get single shop item"""
        shops = Shop.objects.get(pk=pk)
        serializer = ShopSerializer(shops)
        return Response(serializer.data)

    def list(self, request):
        """handle GET requests to get all shopping items
        
        Returns: 
            Response -- JSON serialized list of shops"""
        shops = Shop.objects.all().order_by('title')

        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

class ShopSerializer(serializers.ModelSerializer):
    """JSON serializer for event"""

    class Meta:
        model = Shop
        fields = ('id', 'title', 'price', 'link', 'asap', 'client' )
        depth = 1
