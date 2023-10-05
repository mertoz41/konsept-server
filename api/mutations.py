import graphene
from .types import PostInput, PostType
from .models import Post
class CreatePost(graphene.Mutation):
    class Arguments:
        post_data = PostInput(required=True)

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, post_data=None):
        post_instance = Post(
            title=post_data.title,
            address=post_data.address,
            property_type=post_data.property_type,
            price=post_data.price,
            for_sale=post_data.for_sale,
            room_number=post_data.room_number,
            year_built=post_data.year_built,
            square_meter=post_data.square_meter,
        )
        post_instance.save()
        return CreatePost(post=post_instance)

