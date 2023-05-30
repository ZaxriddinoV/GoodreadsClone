from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from book.models import Book, BookReview
from .forms import BookReviewForm
# Create your views here.

class BooksView(View):
    def get(self,request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q','')
        if search_query:
            books = books.filter(title__icontains=search_query)


        page_size = request.GET.get('page_size',2)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context ={
            'page_obj':page_obj,
            'search_query':search_query
        }
        return render(request, 'book/list.html',context )
class DetailView(View):
    def get(self,request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context = {
            'book':book,
            'review_form':review_form
        }
        return render(request, 'book/detail.html',context)

class CommentView(LoginRequiredMixin,View):
    def post(self,request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse("book:detail", kwargs={'id': book.id }))

        context = {
            'book': book,
            'review_form': review_form
        }
        return render(request, 'book/detail.html', context)



class EditReviewEdit(LoginRequiredMixin,View):
    def get(self, request, book_id,review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)

        context = {
            'book':book,
            "review":review,
            'review_form':review_form
        }
        return render(request, 'book/edit_review.html',context)
    def post(self, request,book_id,review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("book:detail", kwargs={'id': book.id}))

        context = {
            'book': book,
            "review": review,
            'review_form': review_form
        }
        return render(request, 'book/edit_review.html', context)


class ReviewDelete(LoginRequiredMixin,View):
    def get(self,request, book_id,review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)

        context = {
            'book': book,
            "review": review,
            'review_form': review_form
        }
        return render(request, 'book/ReviewDelete.html', context)


class ViewDelete(LoginRequiredMixin,View):
    def get(self,request,book_id,review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)

        review.delete()

        messages.success(request,"You have successfully deleted your message")

        return redirect(reverse("book:detail", kwargs={'id': book.id}))







