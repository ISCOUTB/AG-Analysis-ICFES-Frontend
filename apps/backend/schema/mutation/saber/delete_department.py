import graphene
from schema.types import DepartmentType
from saber.models import Department
from saber.exceptions import DepartmentNotFoundError
from django.core.exceptions import ObjectDoesNotExist


class DeleteDepartmentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    department = graphene.Field(DepartmentType)

    def mutate(self, info, id):
        try:
            department = Department.objects.get(pk=id)
            deleted_department = Department(
                pk=department.id, name=department.name)
            department.delete()
            return DeleteDepartmentMutation(department=deleted_department)

        except ObjectDoesNotExist:
            raise DepartmentNotFoundError(id=str(id))
