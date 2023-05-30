from django.urls import path

from book.views import BooksView,DetailView,CommentView,EditReviewEdit,ReviewDelete,ViewDelete

app_name = "book"
urlpatterns = [
    path('', BooksView.as_view(),name='books' ),
    path("<int:id>/",DetailView.as_view(),name="detail"),
    path('<int:id>/review/',CommentView.as_view(), name="comment"),
    path('<int:book_id>/reviews/<int:review_id>/edit/',EditReviewEdit.as_view(),name='edit_review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/',ReviewDelete.as_view(),name='delete_review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/conform/',ViewDelete.as_view(),name='view_delete'),

]