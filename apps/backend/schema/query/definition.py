import graphene
from books.exceptions import BookNotFoundError
from saber.exceptions import DepartmentNotFoundError, MunicipalityNotFoundError, InstitutionNotFoundError
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

    institutions = graphene.List(types.InstitutionType)
    institution = graphene.Field(types.InstitutionType)

    def resolve_institutions(self, info):
        return types.Institution.objects.all()

    def resolve_institution(self, info, id):
        try:
            return types.Institution.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise InstitutionNotFoundError(institution_id=str(id))

    students = graphene.List(types.InstitutionType,
                             institution_id=graphene.ID())

    def resolve_students(self, info, institution_id):
        try:
            institution = types.Institution.objects.get(pk=institution_id)
            return institution.students.objects.all()
        except ObjectDoesNotExist:
            pass
