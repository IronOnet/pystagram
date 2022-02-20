from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager): 
    pass

class BaseUser(AbstractBaseUser, PermissionsMixin): 
    pass

# Create your models here.
class Post(models.Model): 
    user_id = models.ForeignKey('User', on_delete=models.Case, null=False) 
    media_url = models.CharField(max_length=256, null=False)
    media_longitude = models.IntegerField() 
    medial_latitude = models.IntegerField() 
    user_longitude = models.IntegerField() 
    user_latitude = models.IntegerField() 
    comments = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model): 
    pass 

class Comment(models.Model): 
    pass 

class Follow(models.Model): 
    pass
