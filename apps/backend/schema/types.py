from graphene_django import DjangoObjectType
from books.models import Book
from saber.models import Department, Municipality, Institution, Student


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department


class MunicipalityType(DjangoObjectType):
    class Meta:
        model = Municipality


class InstitutionType(DjangoObjectType):
    class Meta:
        model = Institution


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
