from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Xavfsizlik: faqat `safe` metodlar (GET, HEAD, OPTIONS) hamma uchun,
    lekin o'zgartirish (POST, PUT, DELETE va h.k) faqat admin/staff foydalanuvchilar uchun.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Ob’ektning egasi bo‘lgan foydalanuvchi o‘zgartirish huquqiga ega.
    Boshqalar faqat o‘qiy oladi.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Bu yerda `owner` emas, balki foydalanuvchi bilan bog‘langan maydon nomini aniqlash kerak.
        # Misol uchun, sizning modellarizda `user` yoki `student.user` yoki `teacher.user` bo‘lishi mumkin.

        # Agar ob’ektda `user` maydoni bo‘lsa:
        owner = getattr(obj, 'user', None)
        if owner is None:
            # Agar `user` maydoni yo'q, boshqa nomlar bilan tekshirish mumkin
            # Masalan, 'student' yoki 'teacher'
            if hasattr(obj, 'student'):
                owner = getattr(obj.student, 'user', None)
            elif hasattr(obj, 'teacher'):
                owner = getattr(obj.teacher, 'user', None)

        return owner == request.user
