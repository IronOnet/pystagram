from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager): 
    # this is the command that gets executed whenever you 
    # create a new user from the CLI 
    def create_user(self, email, password=None, **extra_fields): 
        if not email: 
            raise ValueError("Users mus have an email address") 
        
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 

        user.set_password(password) 
        user.save() 
        return user 

    def create_superuser(self, email, password=None, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have "is_staff=True".') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True') 
        return self.create_user(email, password, **extra_fields)



# Create your models here.
class Post(models.Model): 
    
    VIDEO = 'VIDEO' 
    PHOTO = 'PHOTO'
    MEDIA_TYPES = (
        (VIDEO, 'Video'),
        (PHOTO, 'Photo')
    )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False) 
    #media_url = models.CharField(max_length=256, null=False)
    #media_type = models.CharField(max_length=50, choices=MEDIA_TYPES, null=False)
    photo = models.ManyToManyField('Photo') 
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    media_longitude = models.IntegerField() 
    media_latitude = models.IntegerField() 
    user_longitude = models.IntegerField() 
    user_latitude = models.IntegerField() 
    likes = models.ManyToManyField('Like')
    comments = models.ManyToManyField('Comment')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)



class Photo(models.Model): 
    uid = models.UUIDField()  
    content = models.ImageField(upload_to='photos') 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Video(models.Model): 
    uid = models.UUIDField() 
    content = models.FileField(upload_to='videos') 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractBaseUser, PermissionsMixin): 
    ADMIN = "ADMIN" 
    USER = "USER" 
    ROLES = (
        (ADMIN, "Admin"), 
        (USER, "User")
    )

    email = models.EmailField(max_length=255, unique=True, null=False) 
    username = models.CharField(max_length=255, unique=True, null=False)
    first_name = models.CharField(max_length=255, null=False) 
    last_name = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False, blank=False) 
    is_admin = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False) 
    last_login = models.DateTimeField(auto_now=True) 
    role = models.CharField(choices=ROLES, default="User", max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    objects = UserAccountManager() 

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self): 
        return self.email
    

class Comment(models.Model): 
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, null=False) 
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    content = models.CharField(max_length=255, null=False)
    reply = models.ManyToManyField('Comment')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model): 
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE) 
    user_id = models.ForeignKey('User', on_delete=models.CASCADE) 
    is_liked = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Following(models.Model): 
    # TODO: Fix this self reference error
    target = models.ForeignKey('User', on_delete=models.CASCADE, null=False, related_name="followers") 
    follower = models.ForeignKey('User', on_delete=models.CASCADE, null=False, related_name="targets")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class UserProfile(models.Model): 
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False) 
    bio = models.CharField(max_length=144) 
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Bookmark(models.Model):
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model): 
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, null=False) 
    text = models.CharField(max_length=50, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.text