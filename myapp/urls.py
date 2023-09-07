from django.urls import path
from .views import *

urlpatterns = [
    path('books', BookListView.as_view(), name='book-list-view'),
    path('addbook',AddBookView.as_view(),name='addbook'),
    path('book_by_id/<int:book_id>',BookByIdView.as_view(),name='book_by_id'),
    path('book_by_author/<str:author_name>',BookByAuthorName.as_view(),name='book_by_author'),
    path('editbook/<int:book_id>',EditBookView.as_view(),name='editbook'),
    path('deletebook/<int:book_id>',DeleteBookView.as_view(),name='deletebook'),
    path('books_by_date', BookListFilter.as_view(), name='books_by_date'),
    path('book_details/', BookDetails.as_view(), name='book_details'),
    path('book_details/<int:book_id>', BookDetails.as_view(), name='book_details'),
    path('register',registerView.as_view(),name='reg'),
    path('login',loginView.as_view(),name='login'),
    path('getuserdetails',UserDetailsView.as_view(),name='getuserdetails'),
    path('addDetails',addDetailsView.as_view(),name='addDetails'),

    


]
