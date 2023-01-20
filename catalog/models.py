from django.db import models


class Product(models.Model):
    """  Поля:
        - Наименование
        - Описание
        - Изображение (превью)
        - Категория
        - Цена за покупку
        - Дата создания
        - Дата последнего изменения"""

    NULLUBLE = {'blank': True, 'null': True}

    name_product = models.CharField(max_length=250, verbose_name='Наименование', )
    title = models.TextField(verbose_name='Описание', )
    image = models.ImageField(upload_to='media/', verbose_name='Изображение (превью)', **NULLUBLE, )
    category = models.ForeignKey('catalog.Category', verbose_name='Категория', on_delete=models.SET_NULL,null=True )
    price = models.FloatField(verbose_name='Цена за покупку', )
    date_create = models.DateTimeField(verbose_name='Дата создания', )
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения', )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    # def __str__(self):
    #     return f'{self.name_product} {self.price}'


class Category(models.Model):
    """ Поля:
    - Наименование
    - Описание

    """

    category_name = models.CharField(max_length=250, verbose_name='Наименование', )
    title = models.TextField(verbose_name='Описание', )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




