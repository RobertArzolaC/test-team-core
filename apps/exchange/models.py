from django.db import models

from apps.core.models import AuditModel


class Coin(AuditModel):
    name = models.CharField("Nombre de la moneda", max_length=100)
    slug = models.CharField("Slug", max_length=100)
    symbol = models.CharField("Símbolo de la moneda", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def latest_statistic(self):
        return self.statistic_set.latest('updated_at')


class Statistic(AuditModel):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name="Moneda")
    price = models.CharField("Precio", max_length=50)
    price_change = models.CharField("Cambio de Precio ", max_length=50, blank=True, null=True)
    low_high_24h = models.CharField("Bajo y alto en 24h", max_length=50)
    trading_volume_24h = models.CharField("Volumen de comercio en 24h", max_length=50)
    market_cap = models.CharField("Capitalización de mercado", max_length=50)
    market_dominance = models.CharField("Dominio de mercado", max_length=50)
    market_rank = models.CharField("Rango de mercado", max_length=50)
    circulating_supply = models.CharField("Suministro circulante", max_length=50)
    total_supply = models.CharField("Suministro total", max_length=50)
    max_supply = models.CharField("Suministro máximo", max_length=50)

    def __str__(self):
        return f"{self.coin} - {self.updated_at}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Estadística"
        verbose_name_plural = "Estadísticas"

    @classmethod
    def load_data(cls, coin, data):
        cls.objects.update_or_create(coin=coin, defaults=data)
