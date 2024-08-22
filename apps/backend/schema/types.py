from graphene_django import DjangoObjectType
import saber.models as saber_models


class DepartmentType(DjangoObjectType):
    class Meta:
        model = saber_models.Department


class MunicipalityType(DjangoObjectType):
    class Meta:
        model = saber_models.Municipality


class CollegeType(DjangoObjectType):
    class Meta:
        model = saber_models.College


class HighschoolType(DjangoObjectType):
    class Meta:
        model = saber_models.Highschool
