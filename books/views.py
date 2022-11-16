from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializers import *


# Create your views here.

@api_view(['GET'])
def get_all_books(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BooksSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()

    return Response('Book successfully deleted')
