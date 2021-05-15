# Generated by Django 3.2.3 on 2021-05-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Monto total de venta')),
                ('client_change', models.FloatField(verbose_name='Cambio otorgado')),
                ('date', models.DateTimeField(verbose_name='Fecha')),
            ],
        ),
    ]
