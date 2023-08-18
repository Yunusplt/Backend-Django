
#!1808 11:51

#! admin ise islem yapabilsin. yoksa sadece izlesin. 

from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  #!GET ise
            return True
        else:
            return bool(request.user.is_staff)
        

#! 1808 11:57 go to views