from graphene_django import DjangoObjectType
import graphene
from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'notes', 'category')


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    category_by_id = graphene.Field(CategoryType, id=graphene.String(required=True))

    def resolve_all_ingredients(self, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_category_by_name(self, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
    def resolve_category_by_id(self, info, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)