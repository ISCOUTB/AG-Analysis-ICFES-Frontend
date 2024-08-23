import graphene
from schema.mutation.saber.create_department import CreateDepartmentMutation
from schema.mutation.saber.delete_department import DeleteDepartmentMutation
from schema.mutation.saber.update_department import UpdateDepartmentMutation


class Mutation(graphene.ObjectType):
    create_department = CreateDepartmentMutation.Field()
    delete_department = DeleteDepartmentMutation.Field()
    update_department = UpdateDepartmentMutation.Field()
