from django.test import SimpleTestCase
from django.urls import resolve, reverse

from apps.exchange.api.v1.views import exchange_list, exchange_detail


class TestUrls(SimpleTestCase):
    def test_list_exchange_url(self):
        url = reverse('exchanges_list')
        self.assertEquals(resolve(url).func, exchange_list)

    def test_detail_exchange_url(self):
        url = reverse('exchanges_detail', args=['symbol_code'])
        self.assertEquals(resolve(url).func, exchange_detail)
