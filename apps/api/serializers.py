from rest_framework import serializers
from apps.api.models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_name(self, value):
        """
        Check that the product has a valid name
        """
        if not value or value == "":
            raise serializers.ValidationError("The product name can't be empty or null")
        return value

    def validate(self, attrs):
        price = attrs.get("price", None)
        if price < 0:
            raise serializers.ValidationError("The price can't be negative")
        return super().validate(attrs)


class CompleteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
