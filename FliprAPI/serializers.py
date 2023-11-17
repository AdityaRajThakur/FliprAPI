from rest_framework import serializers 
from .models import Customer , Order , Shipping 

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Order 
        fields = '__all__'

    def validate(self ,data):
        if(data['Price'] > data['MRP']):
            return serializers.ValidationError("Price should be smaller than MRP.") 
        return data 
    

class ShippingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shipping 
        fields = '__all__' 

