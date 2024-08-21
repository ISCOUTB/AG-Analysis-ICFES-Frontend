import graphene
from schema.mutation.books.create_book_mutation import CreateBookMutation
from schema.mutation.books.delete_book_mutation import DeleteBookMutation
from schema.mutation.books.update_book_mutation import UpdateBookMutation


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutation.Field()
