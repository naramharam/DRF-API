from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    # 객체의 소유자에게만 쓰기를 허용하는 사용자 정의 권한
    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모두에게 허용하므로, 'GET, 'HEAD', 'OPTIONS' 요청은 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 해당 snippet의 생성자에게만 부여함
        return obj.owner == request.user