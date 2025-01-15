from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Author, Book

class AuthorView(ViewSet):
    """View for handling author requests"""
    def retrieve(self, request, pk):
        """Handle GET requests for single authors"""
        uid = request.query_params.get('uid', None)
        try:
            if uid is None:
                author = Author.objects.get(pk=pk)
            else:
                author = Author.objects.get(pk=pk, uid=uid)
            serializer = SingleAuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        """Handle GET requests to get all authors"""
        uid = request.query_params.get('uid', None)
        try:
            if uid is not None:
                authors = authors.filter(uid=uid)
            else:
                authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST requests to get all authors"""
        author = Author.objects.create(
            email=request.data["email"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            image=request.data["image"],
            favorite=request.data["favorite"],
            uid=request.data["uid"]
    )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests to get all authors"""
        author = Author.objects.get(pk=pk)
        author.email=request.data["email"]
        author.first_name = request.data["first_name"]
        author.last_name = request.data["last_name"]
        author.image = request.data["image"]
        author.favorite = request.data["favorite"]
        author.uid = request.data["uid"]
     
        author.save()
     
        serializer = AuthorSerializer(author)    
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Handle DELETE requests to get all authors"""
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'image', 'favorite', 'uid')

class SingleAuthorSerializer(serializers.ModelSerializer):

    book_count = serializers.IntegerField(default=None)

    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 
                  'last_name', 'image', 'favorite', 
                  'uid', 'book_count', 'books')
        depth = 1
