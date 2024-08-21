import graphene
from graphene_django import DjangoObjectType
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist


class BookNotFoundError(Exception):
    def __init__(self, book_id) -> None:
        super().__init__(f"Book with the given {book_id} doesn't exists")


class BookType(DjangoObjectType):
    class Meta:
        model = Book


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


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, title, description):
        book = Book(title=title, description=description)
        book.save()
        return CreateBookMutation(book=book)


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


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, id, title=None, description=None):
        try:
            book = Book.objects.get(pk=id)

            if title is not None:
                book.title = title

            if description is not None:
                book.description = description

            book.save()

            return UpdateBookMutation(book=book)
        except ObjectDoesNotExist:
            raise BookNotFoundError(book_id=id)


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
