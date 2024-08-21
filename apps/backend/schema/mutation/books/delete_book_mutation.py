import graphene
from schema.types import BookType
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist
from books.exceptions import BookNotFoundError


class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return DeleteBookMutation(book=book)
        except ObjectDoesNotExist:
            raise BookNotFoundError(book_id=id)
