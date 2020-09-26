from django.test import TestCase

from apps.exchange.models import Exchange


class TestModels(TestCase):
    def setUp(self):
        self.exchange_1 = Exchange.objects.create(symbol_code="IRB5IKCO8751",
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

    def test_exchage_symbol_code(self):
        self.assertEquals(self.exchange_1.symbol_code, "IRB5IKCO8751")

    @property
    def total_exchanges(self):
        exchanges_list = Exchange.active.all()
        return exchanges_list.count()

    def test_total_exchanges(self):
        Exchange.objects.create(
            symbol_code="IRR1GDIR0101",
            group="n1",
            group_industry="شرکتهاي چند رشته اي صنعتي",
            board="m",
            latin_symbol="GDIX1",
            latin_name="Ghadir Inv.-R",
            persian_symbol="وغديرح",
            persian_name="ح . سرمايه‌گذاري‌غدير(هلدينگ‌",
            created="2020-09-26T23:35:14.515423+03:30",
            updated="2020-09-26T23:56:46.160937+03:30",
            status=True

        )
        Exchange.objects.create(
            symbol_code="IRO1GDIR0001",
            group="n1",
            group_industry="شرکتهاي چند رشته اي صنعتي",
            board="m",
            latin_symbol="GDIR1",
            latin_name="Ghadir Inv.",
            persian_symbol="وغدير",
            persian_name="سرمايه‌گذاري‌غدير(هلدينگ‌",
            created="2020-09-26T23:35:14.515392+03:30",
            updated="2020-09-26T23:56:46.158025+03:30",
            status=True

        )
        Exchange.objects.create(
            symbol_code="IRR1SNMA0101",
            group="n1",
            group_industry="سرمايه گذاريها",
            board="m",
            latin_symbol="SNMX1",
            latin_name="Ind. & Mine Inv-R",
            persian_symbol="وصنعتح",
            persian_name="ح . سرمايه‌ گذاري‌صنعت‌ ومعدن‌",
            created="2020-09-26T23:35:14.515361+03:30",
            updated="2020-09-26T23:56:46.153641+03:30",
            status=True

        )
        Exchange.objects.create(
            symbol_code="IRO1SNMA0001",
            group="n1",
            group_industry="سرمايه گذاريها",
            board="m",
            latin_symbol="SNMA1",
            latin_name="Ind. & Mine Inv",
            persian_symbol="وصنعت",
            persian_name="سرمايه گذاري توسعه صنعت وتجارت",
            created="2020-09-26T23:35:14.515330+03:30",
            updated="2020-09-26T23:56:46.151613+03:30",
            status=True
        )

        self.assertEquals(self.total_exchanges, 5)