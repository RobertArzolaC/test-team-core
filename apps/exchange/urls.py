from django.urls import path

from apps.exchange import views

app_name = 'apps.exchange'

urlpatterns = [
    path(
        '',
        views.StatisticListView.as_view(),
        name='statistic-list'
    ),
]
