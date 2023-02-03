from django.contrib import admin

from apps.exchange import models


@admin.register(models.Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol", "slug")
    exclude = ("owner", "update_by",)


@admin.register(models.Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("coin", "price", "market_cap", "created_at", "updated_at")
    exclude = ("owner", "update_by",)
