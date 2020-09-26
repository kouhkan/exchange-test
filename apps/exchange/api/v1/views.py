from apps.exchange.models import Exchange
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ExchangeSerializer
from rest_framework import status


@api_view(['GET'])
def exchange_list(request):
    exchanges = Exchange.active.all()
    serializer = ExchangeSerializer(exchanges, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def exchange_detail(request, code):
    try:
        get_exchange = Exchange.active.get(symbol_code=code)
    except Exchange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialize = ExchangeSerializer(get_exchange)
    return Response(data=serialize.data, status=status.HTTP_200_OK)

