from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from app import views

router = DefaultRouter() 
router.register(r'users', views.UserViewSet) 
router.register(r'comments', views.CommentViewSet) 
router.register(r'posts', views.PostViewSet) 
router.register(r'tags', views.TagViewSet) 
router.register(r'following', views.FollowingViewSet)
router.register(r'profiles', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]