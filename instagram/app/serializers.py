
from rest_framework.serializers import ModelSerializer

from instagram.app.models import (Bookmark, Following, Like, Post,\
     Tag, User, Comment, UserProfile)

class PostSerializer(ModelSerializer): 
    class Meta: 
        model = Post 
        fields = ['user_id', 'media_url', 'media_type', 'media_longitude', 'media_latitude',\
            'user_longitude', 'user_latitude', 'comments']

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

class CommentSerializer(ModelSerializer): 
    class Meta: 
        model = Comment
        fields = ['post_id', 'content']

class FollowingSerializer(ModelSerializer): 
    class Meta: 
        model = Following 
        fields = ['target', 'follower']

class UserProfileSerializer(ModelSerializer): 
    class Meta: 
        model = UserProfile 
        fiels = ['user_id', 'bio']

class BookmarkSerializer(ModelSerializer): 
    class Meta: 
        model = Bookmark 
        fields = ['post_id']

class TagSerializer(ModelSerializer): 
    class Meta: 
        model = Tag
        fields = ['post_id', 'text']

class LikeSerializer(ModelSerializer): 
    class Meta: 
        model = Like 
        fields = ['post_id', 'user_id']



