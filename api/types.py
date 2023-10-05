import graphene
from graphene_django import DjangoObjectType, DjangoListField 
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"

class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    address = graphene.String()
    property_type = graphene.String()
    price = graphene.Int()
    for_sale = graphene.Boolean()
    room_number = graphene.Int()
    year_built = graphene.Int()
    square_meter = graphene.Int()
