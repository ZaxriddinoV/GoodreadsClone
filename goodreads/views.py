from django.core.paginator import Paginator
from django.shortcuts import render
from book.views import BookReview

def landing_page(request):
    book_review = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size',10)
    paginator = Paginator(book_review,page_size)
    pag_num = request.GET.get('page',1)
    page_obj = paginator.get_page(pag_num)
    context = {'page_obj':page_obj}
    return render(request, "landing.html",context)