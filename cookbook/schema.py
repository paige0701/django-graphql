import graphene
from ingredients.graphql.schema2 import Query as q


class Query(q, graphene.ObjectType):
    pass


schema2 = graphene.Schema(query=Query)
