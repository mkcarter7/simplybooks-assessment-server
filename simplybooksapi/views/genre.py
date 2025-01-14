from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models.genre import Genre
from simplybooksapi.models.book import Book



class GenreView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  def retrieve(self, request, pk):
    
    try:
      genre = Genre.objects.get(pk=pk)
      books = Book.objects.filter(genrebooks__genre_id=genre)
      genre.books=books.all()
      serializer = SingleGenreSerializer(genre)
      return Response(serializer.data)
    except Genre.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    try:
      genres = Genre.objects.all()
      
      serializer = GenreSerializer(genres, many=True)
      return Response(serializer.data)
    except:
      return Response({'message': 'Check query'}, status=status.HTTP_400_BAD_REQUEST)
    
  #POST REQUESTS
  def create(self, request):
    genre = Genre.objects.create(
      description=request.data["description"],
    )
    serializer = GenreSerializer(genre)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    id = pk
    genre = Genre.objects.get(pk=pk)
    genre.description = request.data["description"]
    
    genre.save()
    
    serializer = GenreSerializer(genre)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    genre = Genre.objects.get(pk=pk)
    genre.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class GenreSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Genre
    fields = ('id', 'description')
    depth = 1

class BookSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Book
    fields = ('id', 'author', 'title', 'image', 'price', 'sale', 'uid', 'description')

class SingleGenreSerializer(serializers.ModelSerializer):
  
  books = BookSerializer(read_only=True, many=True)
  
  class Meta:
    model = Genre
    fields = ('id', 'description', 'books')
    depth = 1
