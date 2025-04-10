from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import exceptions, serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    
    
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    user_id = serializers.IntegerField(read_only=True)  

    def validate_password(self, value):
        if len(value) < 8:
            raise exceptions.ValidationError(_("Password must be at least 8 characters long"))
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_id=validated_data["user_id"],
            password=validated_data["password"]
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ["user_id", "first_name", "last_name", "password"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "user_id": {"required": True}
        }
        
        
        
        

    
class ConfirmSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = get_user_model().objects.filter(phone=value)
        if user.exists():
            return value

        raise serializers.ValidationError(_("User does not exist"))


class ResetConfirmationSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = get_user_model().objects.filter(phone=value)
        if user.exists():
            return value
        raise serializers.ValidationError(_("User does not exist"))


class ResendSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
