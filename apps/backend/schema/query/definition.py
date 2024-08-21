import graphene
from books.exceptions import BookNotFoundError
from saber.exceptions import DepartmentNotFoundError, MunicipalityNotFoundError
import schema.types as types
from django.core.exceptions import ObjectDoesNotExist


class Query(graphene.ObjectType):
    books = graphene.List(types.BookType)
    book = graphene.Field(types.BookType, id=graphene.ID())

    def resolve_books(self, info):
        return types.Book.objects.all()

    def resolve_book(self, info, id):
        try:
            return types.Book.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise BookNotFoundError(book_id=str(id))

    departments = graphene.List(types.DepartmentType)
    department = graphene.Field(types.DepartmentType, id=graphene.ID())

    def resolve_departments(self, info):
        return types.Department.objects.all()

    def resolve_department(self, info, id):
        try:
            return types.Department.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise DepartmentNotFoundError(department_id=str(id))

    municipalities = graphene.List(types.MunicipalityType)
    municipality = graphene.Field(types.MunicipalityType, id=graphene.ID())

    def resolve_municipalities(self, info):
        return types.Department.objects.all()

    def resolve_municipality(self, info, id):
        try:
            return types.Municipality.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise MunicipalityNotFoundError(municipality_id=str(id))
