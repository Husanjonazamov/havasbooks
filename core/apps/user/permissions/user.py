from rest_framework import permissions



class UserPermission(permissions.BasePermission):
    message = _("Permission denied")

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        request.bot_user = None
        pk = get_pk(request)
        if pk is None:
            return False
        try:
            user = BotUserModel.objects.get(pk=pk)
        except BotUserModel.DoesNotExist:
            request.bot_user = pk  
            return True
        request.bot_user = user
        return True

