# import graphene
# from schema.types import BookType
# from books.models import Book


# class CreateBookMutation(graphene.Mutation):
#     class Arguments:
#         title = graphene.String()
#         description = graphene.String()

#     book = graphene.Field(BookType)

#     def mutate(self, info, title, description):
#         book = Book(title=title, description=description)
#         book.save()
#         return CreateBookMutation(book=book)
