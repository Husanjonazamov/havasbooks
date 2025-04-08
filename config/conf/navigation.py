from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()



PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "groups_2",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            # {
            #     "title": _("Foydalanuvchilar"),
            #     "icon": "person_add",
            #     "link": reverse_lazy("admin:auth_user_changelist"),
            #     "permission": lambda request: user_has_group_or_permission(
            #         request.user, "view_user"
            #     ),
            # },
        ],
    },
]
