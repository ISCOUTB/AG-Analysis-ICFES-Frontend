import graphene
from schema.types import DepartmentType
from saber.models import Department
from django.core.exceptions import ObjectDoesNotExist
from saber.exceptions import DepartmentNotFoundError


class UpdateDepartmentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    department = graphene.Field(DepartmentType)

    def mutate(self, info, id, name=None):
        try:
            department = Department.objects.get(pk=id)

            if name is not None:
                department.name = name

            department.save()

            return UpdateDepartmentMutation(department=department)
        except ObjectDoesNotExist:
            raise DepartmentNotFoundError()
