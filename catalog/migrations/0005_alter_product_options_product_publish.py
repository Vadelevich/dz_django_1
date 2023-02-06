# Generated by Django 4.1.5 on 2023-02-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_article_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('change_title_product', 'Can title product'), ('set_category_product', 'Can category product'), ('set_status_product', 'change status product')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='статус'),
        ),
    ]