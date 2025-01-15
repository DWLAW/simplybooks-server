from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import BookGenre, Book, Genre


class GenreBookView(ViewSet):
  def retrieve(self, request, pk):
    """Handle GET requests for single book genre
          
        Returns:
            Response -- JSON serialized book genre
        """
    
    bookGenre = BookGenre.objects.get(pk=pk)
    serializer = GenreBookSerializer(bookGenre)
    return Response(serializer.data)
 
  def list(self, request):
        """Handle GET requests to get all genres 

        Returns:
            Response -- JSON serialized list of genres
        """
        bookGenres = BookGenre.objects.all()
        serializer = GenreBookSerializer(bookGenres, many=True)
        return Response(serializer.data)
  
  def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized genre instance
        """
        bookId = Book.objects.get(pk=request.data["book"])
        genreId = Genre.objects.get(pk=request.data["genre"])

        bookGenre = BookGenre.objects.create(
            book=bookId,
            genre=genreId,
        )
        serializer = GenreBookSerializer(bookGenre)
        return Response(serializer.data)
  
  def update(self, request, pk):
      bookId = Book.objects.get(pk=request.data["book"])
      genreId = Genre.objects.get(pk=request.data["genre"])
      
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.book_id = bookId
      bookGenre.genre_id = genreId

      bookGenre.save()

      serializer = GenreBookSerializer(bookGenre)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
  def destroy(self, request, pk):
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)

class GenreBookSerializer(serializers.ModelSerializer):
    """JSON serializer for genre 
    """
    class Meta:
        model = BookGenre
        fields = ('id', 'book', 'genre' )
        depth = 1
