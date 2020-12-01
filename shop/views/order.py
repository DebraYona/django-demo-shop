from decimal import Decimal

from django.contrib.auth.models import User
from django.http import HttpResponse
from pip._internal.utils import logging
from rest_framework import viewsets
import logging
from random import randint
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.models import Product
from shop.models import Order, OrderDetail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from shop.serializers import OrderWithDetailsSerializer, OrdersSerializer, OrderDetailSerializer


def generate_order_code():
    last = Order.objects.last()
    order_code = "OC-" + str(randint(0, 999999)).zfill(6)
    return order_code


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filter_fields = (
        'creation_date',

        'client',
        'order_status',
    )
    search_fields = ['order_code']
    ordering_fields = (
        'target_total_amount',
        'total_amount',
    )


def createOrder(order):
    try:
        total_amount = 0.0
        order_code = generate_order_code()
        order_status = 1
        if order['client']:

            client_id = order['client']
            client = User.objects.get(id=client_id)
            if order['items_client']:
                items_client = order['items_client']
                new_order = Order.objects.create(order_code=order_code, client=client,
                                             order_status=order_status,
                                             total_amount=total_amount,
                                             )

                for item in items_client:
                    total_amount += item['total_amount']
                    product = Product.objects.get(id=item['product_id'])
                    order_detail = OrderDetail.objects.create(order=new_order, product=product,
                                                              quantity=item['quantity'],
                                                              unit_price_amount=item['unit_price_amount'],
                                                              total_amount=item['total_amount'],
                                                              )
                new_order.total_amount = total_amount
                new_order.save()
            else:
                raise Exception("Empty Item List")

        return new_order
    except Exception as e:
        logging.exception(e)
        content = {'error': str(e)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_fields = ['order_id']


class AddProductToCartAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            client_id = request.data['client']
            items_client = request.data['items_client']
            order = Order.objects.filter(client__id=client_id, order_status=1)
            if len(order) <= 0:
                new_order = createOrder(order=request.data)
            else:
                detail = OrderWithDetailsSerializer(order[0]).data
                total_order = float(detail['total_amount'])

                new_order = order[0]
                total_amount = 0.0

                for item in items_client:
                    total_amount += item['total_amount']
                    product = Product.objects.get(id=item['product_id'])
                    order_detail = OrderDetail.objects.create(order=new_order, product=product,
                                                              quantity=item['quantity'],
                                                              unit_price_amount=item['unit_price_amount'],
                                                              total_amount=item['total_amount'],
                                                              )

                new_order.total_amount = total_amount + total_order
                new_order.save()
            return Response(
                {"message": "Orden Creada correctamente", "order_detail": OrderWithDetailsSerializer(new_order).data},
                status=status.HTTP_200_OK)

        except Exception as e:
            logging.exception(e)
            content = {'error': str(e)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)