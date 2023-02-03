from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from apps.exchange import models
from apps.core.scraper import CoinScraper


class ScrapingByCoinView(View):
    def get(self, request, *args, **kwargs):
        coin = get_object_or_404(models.Coin, slug=kwargs['coin'])
        scraper = CoinScraper()
        data = scraper.extract_coin_data(coin.slug)
        models.Statistic.load_data(coin, data)
        return HttpResponse('ok')


class ScrapingAllCoinsView(View):
    def get(self, request, *args, **kwargs):
        coins = models.Coin.objects.all()
        scraper = CoinScraper()
        for coin in coins:
            data = scraper.extract_coin_data(coin.slug)
            models.Statistic.load_data(coin, data)
            return HttpResponse('ok')
