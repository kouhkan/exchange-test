from django.http import HttpResponse
from apps.exchange.models import Exchange


def inedx(request):
    return HttpResponse('ok')
