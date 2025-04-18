from rest_framework import serializers

from ...models import PreorderModel
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.serializers.book import BaseBookSerializer



class BasePreorderSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    class Meta:
        model = PreorderModel
        fields = [
            "id",
            "user",
            "book",
            'count',
            "user_name",
            "phone"
        ]

    def get_book(self, obj):
        return BaseBookSerializer(obj.book).data

class ListPreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...


class RetrievePreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...


class CreatePreorderSerializer(BasePreorderSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())

    class Meta(BasePreorderSerializer.Meta):
        fields = [
            'id',
            'book',
            'count',
            'user_name',
            'phone'
        ]


    def create(self, validated_data):
        book_data = validated_data.get('book').id
        book = BookModel.objects.get(id=book_data)
        count = validated_data.get('count')
        user_name = validated_data.get('user_name')
        phone = validated_data.get('phone')
        user = self.context['request'].user

        if user.is_anonymous:
            raise serializers.ValidationError("Foydalanuvchi autentifikatsiya qilinmagan.")



        preorder = PreorderModel.objects.create(
            user=user,
            book=book,
            count=count,
            user_name=user_name,
            phone=phone
        )

        return preorder

