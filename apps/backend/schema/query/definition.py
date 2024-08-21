import graphene
from books.exceptions import BookNotFoundError
from schema.types import BookType
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_book(self, info, id):
        try:
            return Book.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise BookNotFoundError(book_id=id)
