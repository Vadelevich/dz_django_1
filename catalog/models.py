from django.conf import settings
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

    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,**NULLUBLE)
    name_product = models.CharField(max_length=250, verbose_name='Наименование', )
    title = models.TextField(verbose_name='Описание', )
    image = models.ImageField(upload_to='media/', verbose_name='Изображение (превью)', **NULLUBLE, )
    category = models.ForeignKey('catalog.Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    price = models.FloatField(verbose_name='Цена за покупку', )
    date_create = models.DateTimeField(verbose_name='Дата создания', )
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения', )
    publish = models.BooleanField(default=False,verbose_name='статус')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('change_title_product','Can title product'),
            ('set_category_product', 'Can category product'),
            ('set_status_product', 'change status product'),
        ]

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

    def __str__(self):
        return self.category_name


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
    published = models.CharField(choices=STATUSES, default=STATUSE_INACTIVE, max_length=10, )
    count = models.BigIntegerField(default=0, verbose_name='количество просмотров')

    class Meta :
        permissions = [
            ('set_published_status','Can publish article'),
        ]


    def save(self, *args, **kwargs):
        """ при создании динамически формирует slug из заголовка """
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class Version(models.Model):
    """ Поля :
    - продукт
    - номер версии
    - название версии
    - признак текущей версии"""

    STATUSE_ACTIVE = 'active'
    STATUSE_INACTIVE = 'inactive'
    STATUSES = (
        ('active', 'активная'),
        ('inactive', 'не активная'),
    )
    product = models.ForeignKey('Product',verbose_name='продукт', on_delete=models.CASCADE,related_name='version')
    number = models.FloatField(verbose_name='номер версии',default=1)
    name = models.CharField(max_length=100,verbose_name='название версии')
    status = models.CharField(choices=STATUSES,default=STATUSE_INACTIVE,verbose_name='текущая версия',max_length=15)

