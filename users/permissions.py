from rest_framework import permissions

class UserAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user:
            return True      
        return False
    
    
class OwnerAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 9:
            return True      
        return False
    
class AdminAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 7:
            return True      
        return False


class TeacherAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 5:
            return True      
        return False
    
    
class AssistantAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 3:
            return True      
        return False
    
    
class StudantAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 3:
            return True      
        return False