# # library_app/urls.py
from django.urls import path
from .views import UserListCreateView, UserDetailView, BookListCreateView, BookDetailView, BookDetailsListCreateView, BookDetailsDetailView, BorrowedBooksListCreateView, BorrowedBooksDetailView

urlpatterns = [
     path('', UserListCreateView.as_view(), name='api-root'),  # Set a default view for the root URL


    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),

    path('book-details/', BookDetailsListCreateView.as_view(), name='book-details-list-create'),
    path('book-details/<int:id>/', BookDetailsDetailView.as_view(), name='book-details-detail'),

    path('borrowed-books/', BorrowedBooksListCreateView.as_view(), name='borrowed-books-list-create'),
    path('borrowed-books/<int:id>/', BorrowedBooksDetailView.as_view(), name='borrowed-books-detail'),
]
