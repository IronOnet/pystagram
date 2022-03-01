from rest_framework import permissions
from rest_framework.permissions import BasePermission 

class IsAuthorOrReadOnly(BasePermission): 
    """
    Allows a Post author to modify it 
    """ 
    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            return True 
        
        # instance author must be the request.user himself/herself 
        return obj.author == request.user