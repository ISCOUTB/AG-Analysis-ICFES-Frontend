# import graphene
# from schema.types import BookType
# from books.models import Book
# from django.core.exceptions import ObjectDoesNotExist
# from books.exceptions import BookNotFoundError


# class UpdateBookMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         title = graphene.String()
#         description = graphene.String()

#     book = graphene.Field(BookType)

#     def mutate(self, info, id, title=None, description=None):
#         try:
#             book = Book.objects.get(pk=id)

#             if title is not None:
#                 book.title = title

#             if description is not None:
#                 book.description = description

#             book.save()

#             return UpdateBookMutation(book=book)
#         except ObjectDoesNotExist:
#             raise BookNotFoundError(book_id=id)
