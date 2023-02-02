from django.views.generic.list import ListView

from apps.exchange import models


class StatisticListView(ListView):
    model = models.Statistic
    template_name = 'home/index.html'
