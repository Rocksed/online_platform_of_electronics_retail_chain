# Generated by Django 4.2.5 on 2023-10-06 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementsie',
            options={'verbose_name': 'Индивидуальный предприниматель', 'verbose_name_plural': 'Индивидуальный предприниматель'},
        ),
        migrations.AlterModelOptions(
            name='elementsretail',
            options={'verbose_name': 'Розничная сеть', 'verbose_name_plural': 'Розничная сеть'},
        ),
        migrations.AlterModelOptions(
            name='factoryelements',
            options={'verbose_name': 'Завод', 'verbose_name_plural': 'Завод'},
        ),
        migrations.AlterField(
            model_name='elementsie',
            name='debt_to_supplier',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность перед поставщиком '),
        ),
        migrations.AlterField(
            model_name='elementsie',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trade_network.factoryelements', verbose_name='поставщик'),
        ),
        migrations.AlterField(
            model_name='elementsie',
            name='time_of_creation',
            field=models.TimeField(auto_now_add=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='elementsretail',
            name='debt_to_supplier',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность перед поставщиком '),
        ),
        migrations.AlterField(
            model_name='elementsretail',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trade_network.factoryelements', verbose_name='поставщик'),
        ),
        migrations.AlterField(
            model_name='elementsretail',
            name='time_of_creation',
            field=models.TimeField(auto_now_add=True, verbose_name='время создания'),
        ),
    ]
