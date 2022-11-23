from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """管理者以外読み取り専用"""

    def has_permission(self, request, view):
        """GET, HEAD, OPTIONS は常に許可"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # 管理者のみすべて許可
        return request.user.is_superuser

class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    """管理者とスタッフ以外読み取り専用"""

    def has_permission(self, request, view):
        """GET, HEAD, OPTIONS は常に許可"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # 管理者のみすべて許可
        return request.user.is_staff or request.user.is_superuser