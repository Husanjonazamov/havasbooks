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
        "title": _("Foydalanuvchilar"),
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
    {
        "title": _("Kitoblar bo'limi"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Bannerlar"),
                "icon": "campaign", 
                "link": reverse_lazy("admin:havasbook_bannermodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Kitoblar"),
                "icon": "book",  # Kitoblar uchun mos icon
                "link": reverse_lazy("admin:havasbook_bookmodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Kategoryalar"),
                "icon": "category",  # Kategoryalar uchun mos icon
                "link": reverse_lazy("admin:havasbook_categorymodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
        ]

    },
]
