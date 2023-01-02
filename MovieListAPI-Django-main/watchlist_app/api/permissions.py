from rest_framework import permissions


class IsAdminReadOnly(permissions.IsAdminUser):
    
    ##########this code also work####
    # def has_permission(self, request, view):
    #     return super().has_permission(request, view)
    
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        
        return request.method == 'GET' or admin_permission
    
    

class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
    # Check permissions for read-only request
    
        else:
            return obj.review_user == request.user
    # Check permissions for write request
        # return super().has_object_permission(request, view, obj)