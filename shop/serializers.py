from django.contrib.auth.models import User
from rest_framework import serializers

from core.serializer import UserSerializer
from shop.models import OrderDetail, Order


class SimpleOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'product', 'quantity', 'unit_price_amount', 'total_amount')


class OrdersSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='client')
    creation_date = serializers.DateField(format="%Y-%m-%d")
    legal_creation_date = serializers.DateTimeField(format="%Y-%m-%d")
    detail = SimpleOrderDetailSerializer(many=True, read_only=True, )

    class Meta:
        model = Order
        fields = ('id','order_code', 'creation_date',
                  'legal_creation_date', 'total_amount'
                  , 'order_status', 'client', 'client_id', 'detail')


class OrderWithDetailsSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateField(format="%Y-%m-%d")
    order_status = serializers.CharField(source='get_order_status_display')
    legal_creation_date = serializers.DateTimeField(format="%Y-%m-%d")
    detail = SimpleOrderDetailSerializer(many=True, read_only=True,)

    class Meta:
        model = Order
        fields = ('id', 'order_code', 'legal_creation_date','creation_date',
                  'total_amount','client_id','order_status','detail')

    def get_order_status(self,obj):
        return obj.get_order_status_display()


class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrdersSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Order.objects.all(), source='order')

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'order_id', 'product', 'quantity', 'unit_price_amount', 'total_amount')