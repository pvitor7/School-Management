from rest_framework import permissions

class UserAccount(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True      
        return False
    
    
class UserAccountOrAdmin(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.role.permission >= 7:
            return True      
        return False
        

class UserAccountOrAassistant(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.role.permission >= 3:
            return True      
        return False


class OwnerAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role.permission == 9:
            return True      
        return False
    
class AdminAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role.permission >= 7:
            return True      
        return False


class TeacherAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role.permission >= 5:
            return True      
        return False
    
    
class AssistantAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role.permission >= 3:
            return True      
        return False
    
    
class StudantAuthenticated(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.user.role.permission >= 1:
            return True      
        return False
    