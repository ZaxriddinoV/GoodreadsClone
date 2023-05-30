from rest_framework import serializers

from book.models import Book, BookReview
from users.models import CustomUser


class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','dascription','inbn','book_picter')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email')


class Booksserializers(serializers.Serializer):
    stars_given = serializers.CharField()
    comment = serializers.CharField()
    user = UserSerializers()
    book = Bookserializers()
    class Meta:
        model = BookReview
        fields = ('book','book','user')


