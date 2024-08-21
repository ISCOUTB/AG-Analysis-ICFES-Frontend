from graphene_django import DjangoObjectType
from books.models import Book
from saber.models import Department, Municipality, Institution, Student, StudentResults, Saber11Results, SaberProResults
import graphene


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


class StudentResultsType(DjangoObjectType):
    class Meta:
        model = StudentResults


class Saber11ResultsType(DjangoObjectType):
    class Meta:
        model = Saber11Results


class SaberProResultsType(DjangoObjectType):
    class Meta:
        model = SaberProResults


class ResultsUnion(graphene.Union):
    class Meta:
        types = (Saber11ResultsType, SaberProResultsType)

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, Saber11Results):
            return Saber11ResultsType

        if isinstance(instance, SaberProResults):
            return SaberProResultsType

        return None


class StudentType(DjangoObjectType):
    student_results = graphene.Field(ResultsUnion)

    class Meta:
        model = Student

    def resolve_student_results(self, info):
        return self.results
