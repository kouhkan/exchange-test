import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from apps.exchange.models import Exchange


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('exchanges_list')
        self.detail_url = reverse('exchanges_detail', args=['IRB5IKCO8751'])

        Exchange.objects.create(symbol_code="IRB5IKCO8751",
                                group="n2",
                                group_industry="خودرو و ساخت قطعات",
                                board="f",
                                latin_symbol="IKCQ1",
                                latin_name="Iran Khodro-D",
                                persian_symbol="18719101",
                                persian_name="اوراق مشاركت ايران‌ خودرو",
                                created="2020-09-26T23:35:14.480064+03:30",
                                updated="2020-09-26T23:56:44.447981+03:30",
                                status=True)

    def test_GET_list_view(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_GET_detail_view(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

