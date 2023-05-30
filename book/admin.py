from django.contrib import admin
from .models import Book,Author,BookAutor,BookReview
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    search_fields = ("title",'inbn'),
    list_display = ("title",'inbn','dascription')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name'),

class BookAutorAdmin(admin.ModelAdmin):
    pass
class BookReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookAutor,BookAutorAdmin)
admin.site.register(BookReview,BookReviewAdmin)

