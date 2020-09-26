from django.contrib import admin
from .models import Exchange


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('symbol_code', 'group', 'latin_symbol',
                    'persian_symbol')
    list_filter = ('group', 'board', 'created', 'status')
    list_editable = ('status', )
    search_fields = ('symbol_code', 'latin_symbol', 'latin_name',
                     'persian_symbol', 'persian_name')
    list_per_page = 20
    