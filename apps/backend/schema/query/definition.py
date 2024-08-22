import graphene
from saber.exceptions import DepartmentNotFoundError, MunicipalityNotFoundError, InstitutionNotFoundError, CollegeNotFoundError, StudentsReportsNotFound
import schema.types as types
import saber.models as saber_models
from django.core.exceptions import ObjectDoesNotExist


class Query(graphene.ObjectType):
    # -----------------------------------------------------------------------------|>
    # Department
    # -----------------------------------------------------------------------------|>

    departments = graphene.List(types.DepartmentType)
    department = graphene.Field(types.DepartmentType, id=graphene.ID())

    def resolve_departments(self, info):
        return saber_models.Department.objects.all()

    def resolve_department(self, info, id):
        try:
            return saber_models.Department.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise DepartmentNotFoundError(department_id=str(id))

    # -----------------------------------------------------------------------------|>
    # Municipality
    # -----------------------------------------------------------------------------|>

    municipalities = graphene.List(types.MunicipalityType)
    municipality = graphene.Field(types.MunicipalityType, id=graphene.ID())

    def resolve_municipalities(self, info):
        return saber_models.Municipality.objects.all()

    def resolve_municipality(self, info, id):
        try:
            return saber_models.Municipality.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise MunicipalityNotFoundError(municipality_id=str(id))
