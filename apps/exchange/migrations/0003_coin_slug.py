# Generated by Django 4.1.6 on 2023-02-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0002_alter_statistic_options_statistic_price_change"),
    ]

    operations = [
        migrations.AddField(
            model_name="coin",
            name="slug",
            field=models.CharField(
                default="", max_length=100, verbose_name="Nombre de la moneda"
            ),
            preserve_default=False,
        ),
    ]
