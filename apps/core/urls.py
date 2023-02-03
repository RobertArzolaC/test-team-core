from django.urls import path

from apps.core import views

app_name = 'apps.core'

urlpatterns = [
    path(
        "scraping-by-coin/<str:coin>",
        views.ScrapingByCoinView.as_view(),
        name="scraping-by-coin"
    ),
    path(
        "scraping-all-coins/",
        views.ScrapingAllCoinsView.as_view(),
        name="scraping-all-coins"
    )
]
