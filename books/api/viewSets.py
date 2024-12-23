from rest_framework import viewsets
from books.models import Books
from books.api.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
