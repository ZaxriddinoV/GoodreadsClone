from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookReview
from api.serializers import Booksserializers

class BookReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Booksserializers
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'



# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = Booksserializers
#     queryset = BookReview.objects.all()
#     lookup_field = 'id'
#     def get(self,request,id):
#         book_review = BookReview.objects.get(id=id)
#
#         serializer = Booksserializers(book_review)
#         return Response(data=serializer.data)
#
#
# class BookListAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = Booksserializers
#     queryset = BookReview.objects.all().order_by('-created_at')
#
#     def get(self,request):
#         book_review = BookReview.objects.all().order_by('-created_at')
#         paginator = PageNumberPagination()
#         page_obj = paginator.paginate_queryset(book_review,request)
#
#
#         serializers = Booksserializers(page_obj,many=True)
#         return paginator.get_paginated_response(serializers.data)