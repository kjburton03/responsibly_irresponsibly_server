# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from responsiblyapi.models import Todo, Client

class TodoView(ViewSet):

    def retrieve(self, request, pk):
        """get single shop item"""

        todos = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todos)
        return Response(serializer.data)
    def list(self, request):
        """handle GET requests to get all shopping items
        
        Returns: 
            Response -- JSON serialized list of shops"""
        todos = Todo.objects.all().order_by('title')

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    def create(self, request):
        """

        Args:
            request (_type_): _description_
        """
        client = Client.objects.get(user=request.auth.user)

        todo = Todo.objects.create(
            title=request.data["title"],
            price=request.data["price"],
            daily=request.data["daily"],
            client=client
        )
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

class TodoSerializer(serializers.ModelSerializer):
    """JSON serializer for event"""

    class Meta:
        model = Todo
        fields = ('id', 'title', 'price', 'daily', 'client' )
        depth = 1
