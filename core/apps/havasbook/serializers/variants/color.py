from rest_framework import serializers

from ...models import ColorModel


class BaseColorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = ColorModel
        exclude = [
            "created_at",
            "updated_at",
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class ListColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class RetrieveColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class CreateColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...
