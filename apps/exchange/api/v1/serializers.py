from rest_framework import serializers
from apps.exchange.models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('symbol_code', 'group', 'group_industry',
                  'board', 'latin_symbol', 'latin_name',
                  'persian_symbol', 'persian_name',
                  'created', 'updated', 'status')