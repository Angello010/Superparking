# Generated by Django 5.2.1 on 2025-06-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_de_factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_factura', models.TextField(verbose_name='Tipo_de_factura')),
                ('medio_de_pago', models.TextField(verbose_name='Medios_de_pago')),
            ],
        ),
    ]
