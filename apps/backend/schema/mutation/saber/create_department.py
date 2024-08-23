import graphene
from schema.types import DepartmentType
from saber.models import Department


class CreateDepartmentMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    department = graphene.Field(DepartmentType)

    def mutate(self, info, name):
        department = Department(name=name)
        department.save()
        return CreateDepartmentMutation(department=department)
