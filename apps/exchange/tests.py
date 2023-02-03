from django.test import Client, TestCase
from django.urls import reverse_lazy


from apps.exchange import models


class ScrapingByCoinViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.coin = models.Coin.objects.create(
            name='Bitcoin', symbol='BTC', slug='bitcoin'
        )
        self.url = reverse_lazy(
            'apps.core:scraping-by-coin', kwargs={'coin': self.coin.slug}
        )
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ok')

        objects = models.Statistic.objects.all()
        
        self.assertEqual(objects.count(), 1)
        self.assertEqual(objects[0].coin, self.coin) 

    def test_get_with_invalid_coin(self):
        url = reverse_lazy('apps.core:scraping-by-coin', kwargs={'coin': 'invalid'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ScrapingAllCoinsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.coin = models.Coin.objects.create(
            name='Bitcoin', symbol='BTC', slug='bitcoin'
        )
        self.url = reverse_lazy('apps.core:scraping-all-coins')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ok')

        objects = models.Statistic.objects.all()
        
        self.assertEqual(objects.count(), 1)
        self.assertEqual(objects[0].coin, self.coin)
