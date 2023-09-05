from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import *
from django.shortcuts import get_object_or_404
from datetime import datetime


class BookListView(APIView):

    def get(self, request):
        try:
            books = Book.objects.filter(is_deleted=False)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)      
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class AddBookView(APIView):

    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "A book has been added", "data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e),"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookByIdView(APIView):
    def get(self, request, book_id):
        try:
            book = get_object_or_404(Book, pk=book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookByAuthorName(APIView):
    def get(self, request, author_name):
        try:
            book = Book.objects.filter(author=author_name)
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditBookView(APIView):
    def put(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteBookView(APIView):
    def delete(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            book.is_deleted = True
            book.save()
            return Response({"message":"Book deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


class BookListFilter(APIView):

    def post(self, request):
        try:
            from_date_str = request.data.get('from_date', '')
            to_date_str = request.data.get('to_date', '')

            # Convert the date strings to datetime objects if they are provided
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d') if from_date_str else None
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d') if to_date_str else None

            # Build the queryset with filters based on provided date range
            books = Book.objects.all()

            if from_date:
                books = books.filter(publication_date__gte=from_date)
            if to_date:
                books = books.filter(publication_date__lte=to_date)

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BookDetails(APIView):
    def get(self, request):
        try:
            books = Book.objects.filter(is_deleted=False)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)      
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "A book has been added", "data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e),"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

        
    def delete(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            book.is_deleted = True
            book.save()
            return Response({"message":"Book deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

        