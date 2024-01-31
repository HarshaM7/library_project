# library_app/views.py
from rest_framework import generics
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookDetailsListCreateView(generics.ListCreateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer

class BookDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'id'

class BorrowedBooksListCreateView(generics.ListCreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class BorrowedBooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    lookup_field = 'id'
