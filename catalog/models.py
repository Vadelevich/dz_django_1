from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    category = models.ForeignKey('catalog.Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
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


class Article(models.Model):
    """  Поля :
    - заголовок
    - slug (реализовать через CharField)
    - содержимое
    - превью (изображение)
    - дата создания
    - признак публикации
    - количество просмотров

    """
    STATUSE_ACTIVE = 'active'
    STATUSE_INACTIVE = 'inactive'
    STATUSES = (
        ('active', 'Опубликованный'),
        ('inactive', 'Не опубликованный'),
    )

    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug', editable=False, default='', )
    content = models.TextField(blank=True, verbose_name='Контент')
    image = models.ImageField(upload_to='media/', verbose_name='изображение', blank=True)
    date_create = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    publicate = models.CharField(choices=STATUSES, default=STATUSE_ACTIVE, max_length=10, )
    count = models.BigIntegerField(default=0, verbose_name='количество просмотров')

    def save(self, *args, **kwargs):
        """ при создании динамически формирует slug из заголовка """
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)