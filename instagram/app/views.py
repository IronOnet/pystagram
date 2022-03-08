from crypt import methods
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from app.models import (
    Post, 
    User, 
    Comment, 
    Tag,
    Following, 
    UserProfile, 
    Like
)

from app.serializers import (
    LikeSerializer,
    PostSerializer, 
    UserSerializer, 
    CommentSerializer, 
    TagSerializer, 
    FollowingSerializer, 
    UserProfileSerializer
)


# Handling scenario User can CRUD a Post

class PostViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    like_serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = self.queryset 

        tag = self.request.query_params('tag', None) 
        if tag: 
            pattern = r'(?:\s|^)#[({0})\-\.\_]+(?:\s|$)'.format(tag) 
            queryset = queryset.filter(caption__iregex=pattern)
        return queryset 

    # If the user likes a post, send the like to the 
    # database (Likes table)
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated]) 
    def like(self, request, pk=None): 
        post = self.get_object() 
        obj, created = Like.objects.get_or_create(
            user=request.user, 
            post_id=post.id,
        )

        if not created: 
            obj.is_active = not obj.is_active 
            obj.save()

        return Response(obj.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def comment_post(self, request, pk=None): 
        post = self.get_object() 
        obj, created = Comment.objects.get_or_create(
            user=request.user, 
            post_id = post.id
        )

    

        

    def list(self, request, *args, **kwargs): 
        pass 

    def update(self, request): 
        pass

    def create(self, request, *args, **kwargs): 
        pass 

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CommentViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer 

class UserViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = User.objects.all() 
    serializer_class = UserSerializer 

class TagViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = Tag.objects.all() 
    serializer_class = TagSerializer 


class FollowingViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated]
    queryset = Following.objects.all() 
    serializer_class = FollowingSerializer 

class UserProfileViewSet(ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = UserProfile.objects.all() 
    serializer_class = UserProfileSerializer