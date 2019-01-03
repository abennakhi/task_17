from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Only the owner has access to this page!!! SCRAM!!!"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_staff:
            return True
        else:
            return False