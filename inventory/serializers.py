from rest_framework import serializers
from .models import Product  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Correct attribute name for the model
        fields = '__all__'
