import graphene
from schema.query.definition import Query
from schema.mutation.definition import Mutation


schema = graphene.Schema(query=Query)
