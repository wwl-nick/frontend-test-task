from rest_framework import permissions


class OnlyAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user == view.get_object().author
        return True
