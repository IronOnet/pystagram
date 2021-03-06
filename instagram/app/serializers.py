
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import (Bookmark, Following, Like, Photo, Post,\
     Tag, User, Comment, UserFeed, UserProfile, Video)

class PostSerializer(ModelSerializer): 
   

    class Meta: 
        model = Post 
        fields = '__all__'

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
        fields = ['user_id', 'bio']

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
        fields = ['user_id', 'post_id', 'is_liked']

class PhotoSerializer(ModelSerializer): 
    class Meta: 
        model = Photo 
        fields = ['uid', 'content', 'user_id']

class VideoSerializer(ModelSerializer): 
    class Meta: 
        model = Video 
        fields = ['uid', 'content', 'user_id']

    
class UserFeedSerializer(ModelSerializer): 
    class Meta: 
        model = UserFeed 
        fields = '__all__'


