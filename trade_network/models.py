from django.db import models

NULLABLE = {'blank': True, 'null': True}


class FactoryElements(models.Model):
    name_of_factory = models.CharField(max_length=50, verbose_name='название завода')
    electronic_mail = models.EmailField(verbose_name='Email завода')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    product_model = models.CharField(max_length=50, verbose_name='модель продукта')
    date_of_product_launch = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return self.name_of_factory

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Завод'


class ElementsRetail(models.Model):
    retailer_name = models.CharField(max_length=50, verbose_name='название розничной сети')
    electronic_mail = models.EmailField(verbose_name='Email розничной сети')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    product_model = models.CharField(max_length=50, verbose_name='модель продукта')
    date_of_product_launch = models.DateField(verbose_name='дата выхода продукта на рынок')
    supplier = models.ForeignKey(FactoryElements, on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2,
                                           verbose_name='задолженность перед поставщиком ')
    time_of_creation = models.TimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.retailer_name

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничная сеть'


class ElementsIE(models.Model):
    name = models.CharField(max_length=50, verbose_name='название ИП')
    electronic_mail = models.EmailField(verbose_name='Email ИП')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.IntegerField(verbose_name='номер дома')
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    product_model = models.CharField(max_length=50, verbose_name='модель продукта')
    date_of_product_launch = models.DateField(verbose_name='дата выхода продукта на рынок')
    supplier = models.ForeignKey(FactoryElements, on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2,
                                           verbose_name='задолженность перед поставщиком ')
    time_of_creation = models.TimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальный предприниматель'
