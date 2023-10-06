# Generated by Django 4.2.5 on 2023-10-05 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactoryElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_factory', models.CharField(max_length=50, verbose_name='название завода')),
                ('electronic_mail', models.EmailField(max_length=254, verbose_name='Email завода')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('city', models.CharField(max_length=50, verbose_name='город')),
                ('street', models.CharField(max_length=50, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
                ('product_name', models.CharField(max_length=50, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=50, verbose_name='модель продукта')),
                ('date_of_product_launch', models.DateField(verbose_name='дата выхода продукта на рынок')),
            ],
        ),
        migrations.CreateModel(
            name='ElementsRetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_name', models.CharField(max_length=50, verbose_name='название розничной сети')),
                ('electronic_mail', models.EmailField(max_length=254, verbose_name='Email розничной сети')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('city', models.CharField(max_length=50, verbose_name='город')),
                ('street', models.CharField(max_length=50, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
                ('product_name', models.CharField(max_length=50, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=50, verbose_name='модель продукта')),
                ('date_of_product_launch', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade_network.factoryelements')),
            ],
        ),
        migrations.CreateModel(
            name='ElementsIE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название ИП')),
                ('electronic_mail', models.EmailField(max_length=254, verbose_name='Email ИП')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('city', models.CharField(max_length=50, verbose_name='город')),
                ('street', models.CharField(max_length=50, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
                ('product_name', models.CharField(max_length=50, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=50, verbose_name='модель продукта')),
                ('date_of_product_launch', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade_network.elementsretail')),
            ],
        ),
    ]
