# Generated by Django 4.1.6 on 2023-02-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="statistic",
            options={
                "ordering": ["-id"],
                "verbose_name": "Estadística",
                "verbose_name_plural": "Estadísticas",
            },
        ),
        migrations.AddField(
            model_name="statistic",
            name="price_change",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Cambio de Precio "
            ),
        ),
    ]