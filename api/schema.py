import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType, post_id=graphene.Int())

    def resolve_all_posts(self, info,**kwargs):
        return Post.objects.all()
    
    def resolve_book(self, info, post_id):
        return Post.objects.get(pk=post_id)
    

schema = graphene.Schema(query=Query)
