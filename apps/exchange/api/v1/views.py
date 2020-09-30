from apps.exchange.models import Exchange
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

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


@api_view(['POST'])
def exchange_create(request):
    serializer = ExchangeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
