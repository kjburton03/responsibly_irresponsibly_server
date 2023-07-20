# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
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
    def create(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        client = Client.objects.get(user=request.auth.user)

        shop = Shop.objects.create(
            title=request.data["title"],
            price=request.data["price"],
            asap=request.data["asap"],
        )
        shop.client.set([client])

        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):

        shop = Shop.objects.get(pk=pk)
        shop.title = request.data["title"]
        shop.price = request.data["price"]
        shop.asap=request.data["asap"]


        shop.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        shop = Shop.objects.get(pk=pk)
        shop.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ShopSerializer(serializers.ModelSerializer):
    """JSON serializer for event"""

    class Meta:
        model = Shop
        fields = ('id', 'title', 'price', 'asap', 'client' )
        depth = 1
