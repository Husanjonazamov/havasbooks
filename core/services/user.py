from datetime import datetime
from core.services import sms
from django.contrib.auth import get_user_model, hashers
from django.utils.translation import gettext as _
from django_core import exceptions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt import tokens
from django.db import transaction


class UserService(sms.SmsService):
    def get_token(self, user):
        """
        Foydalanuvchi uchun refresh va access tokenlarini yaratish
        """
        refresh = tokens.RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def create_user(self, first_name, last_name, password, user_id):
        """
        Foydalanuvchi yaratish, telefon tasdiqlashsiz
        """
        try:
            with transaction.atomic():  # Transaction blokini boshlaymiz
                # Foydalanuvchini yaratish yoki mavjud bo'lsa yangilash
                user, created = get_user_model().objects.update_or_create(
                    user_id=user_id,
                    defaults={
                        "user_id": user_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "password": hashers.make_password(password),
                    },
                )
                if created:
                    # Yangi foydalanuvchi yaratildi
                    return user
                # Foydalanuvchi allaqachon mavjud
                return None
        except Exception as e:
            # Xatolik yuz berganda, uni batafsilroq loglash
            print(f"Xatolik yuz berdi: {str(e)}")
            raise PermissionDenied(_("Foydalanuvchi yaratishda xatolik yuz berdi: {}".format(str(e))))

    def send_confirmation(self, phone) -> bool:
        """
        SMS orqali tasdiqlash kodini yuborish
        """
        # SMS yubormaslik uchun faqat metodni xato qilishni ishlatmaslik
        return False

    def validate_user(self, user) -> dict:
        """
        Foydalanuvchining tasdiqlanganligini tekshirish va token yaratish
        """
        if user.validated_at is None:
            user.validated_at = datetime.now()
            user.save()
        token = self.get_token(user)
        return token

    def is_validated(self, user) -> bool:
        """
        Foydalanuvchi tasdiqlanganligini tekshirish
        """
        if user.validated_at is not None:
            return True
        return False

    def change_password(self, user_id, password):
        """
        Foydalanuvchining parolini o'zgartirish
        """
        user = get_user_model().objects.filter(user_id=user_id).first()
        if user:
            user.set_password(password)
            user.save()
        else:
            raise PermissionDenied(_("Foydalanuvchi topilmadi"))
