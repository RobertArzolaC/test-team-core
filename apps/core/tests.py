from django.test import TestCase

from apps.exchange import models
from apps.core.scraper import CoinScraper


class ScraperTestCase(TestCase):

    def setUp(self):
        self.coin = models.Coin.objects.create(
            name='Bitcoin',
            symbol='BTC',
            slug='bitcoin',
        )

    def test_scraper(self):
        scraper = CoinScraper()
        data = scraper.extract_coin_data(self.coin.slug)
        models.Statistic.load_data(self.coin, data)

        obj = models.Statistic.objects.get(coin=self.coin)
        self.assertEqual(obj.price, data['price'])
        self.assertEqual(obj.price_change, data['price_change'])
        self.assertEqual(obj.low_high_24h, data['low_high_24h'])
