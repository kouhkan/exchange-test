from apps.exchange.models import Exchange
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ExchangeSerializer


@api_view(['GET'])
def exchange_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 25
    exchange_items = Exchange.active.all()
    result_page = paginator.paginate_queryset(exchange_items, request)

    serializer = ExchangeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def exchange_detail(request, code):
    try:
        get_exchange = Exchange.active.get(symbol_code=code)
    except Exchange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialize = ExchangeSerializer(get_exchange)
    return Response(data=serialize.data, status=status.HTTP_200_OK)


@swagger_auto_schema(methods=['POST'], request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, properties={
        'symbol_code': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 12'),
        'group': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 2 -> n1 or n2'),
        'group_industry': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 128'),
        'board': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 1 -> f or m or s'),
        'latin_symbol': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 5'),
        'latin_name': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 128'),
        'persian_symbol': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 24'),
        'persian_name': openapi.Schema(type=openapi.TYPE_STRING, description='max length = 64'),
        'created': openapi.Schema(type=openapi.FORMAT_DATETIME, description='Automatically added'),
        'updated': openapi.Schema(type=openapi.FORMAT_DATETIME, description='Automatically added'),
        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='True or False'),
    }
))
@api_view(['POST'])
def exchange_create(request):
    serializer = ExchangeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def exchange_update(request, code):
    try:
        get_exchange = Exchange.active.get(symbol_code=code)
    except Exchange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExchangeSerializer(get_exchange, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def exchange_modify(request, code):
    try:
        get_exchange = Exchange.active.get(symbol_code=code)
    except Exchange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExchangeSerializer(get_exchange, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

