# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
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
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        client = Client.objects.get(user=request.auth.user)

        todo = Todo.objects.create(
            title=request.data["title"],
            price=request.data["price"],
            daily=request.data["daily"],
        )
        todo.client.set([client])  # Use the set() method to assign the related client object

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, pk):
        """Handle DELETE requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
   




class TodoSerializer(serializers.ModelSerializer):
    """JSON serializer for event"""

    class Meta:
        model = Todo
        fields = ('id', 'title', 'price', 'daily', 'client' )
        depth = 1