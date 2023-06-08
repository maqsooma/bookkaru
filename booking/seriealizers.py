from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    amenities = serializers.DecimalField(max_digits=5, decimal_places=2)
    
    discounted_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = ['operator','srevicetype','price','discounted_price','amenities']
        
        
    def get_discounted_price(self,obj):
        
        if obj.price and obj.amenities:
            discount = (int(obj.amenities)/100) * int(obj.price)
            return round(int(obj.price) - discount,2)
        
        else:
            return None
        
        
        
        
        
    