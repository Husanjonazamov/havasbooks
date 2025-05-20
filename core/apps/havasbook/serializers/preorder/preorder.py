from rest_framework import serializers

from ...models import PreorderModel
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.serializers.book import BaseBookSerializer

from core.apps.havasbook.models import ColorModel, SizeModel




class BasePreorderSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = PreorderModel
        fields = [
            "id",
            "book",
            "created_at",
            "user_name",
            "phone",
            "count",
            "status",
            "total_price"
        ]

    def get_book(self, obj):
        book = obj.book
        request = self.context.get('request') 

        image_url = book.image.url if book.image else None
        if image_url and request:
            image_url = request.build_absolute_uri(image_url)

        return {
            "id": book.id,  
            "name": book.name,  # type: str
            "image": image_url,  # type: str
            "color": obj.color.name if obj.color else None,  # type: str | None
            "size": obj.size.name if obj.size else None,  # type: str | None
            "price": str(book.price),  # type: str
            "original_price": str(book.original_price),  # type: str
            "discount_percent": str(book.discount_percent),  # type: str
            "description": book.description,  # type: str
        }


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Fields with the correct types as str
        representation["created_at"] = str(instance.created_at)  # type: str
        representation["user_name"] = str(instance.user_name)  # type: str
        representation["phone"] = str(instance.phone)  # type: str
        representation["count"] = str(instance.count)  # type: str
        representation["status"] = str(instance.status)  # type: str
        representation["total_price"] = str(instance.total_price)  # type: str
        
        return representation

class ListPreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...


class RetrievePreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...

class CreatePreorderSerializer(BasePreorderSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())
    color = serializers.PrimaryKeyRelatedField(
        queryset=ColorModel.objects.all(), required=False, allow_null=True
    )
    size = serializers.PrimaryKeyRelatedField(
        queryset=SizeModel.objects.all(), required=False, allow_null=True
    )

    class Meta(BasePreorderSerializer.Meta):
        fields = [
            'id',
            'book',
            'color', 
            'size',
            'count',
            'user_name',
            'phone'
        ]

    def create(self, validated_data):
        user = self.context['request'].user

        book = validated_data['book']
        book_price = book.price  

        count = validated_data['count']
        total_price = book_price * count  

        preorder = PreorderModel.objects.create(
            user=user,
            book=book,
            count=count,
            user_name=validated_data['user_name'],
            phone=validated_data['phone'],
            color=validated_data.get('color') or None,
            size=validated_data.get('size') or None,
            total_price=total_price 
        )

        return preorder
