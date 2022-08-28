# Generated by Django 3.2.13 on 2022-07-12 13:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220712_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#0000FF', 'Синий'), ('#FFA500', 'Оранжевый'), ('#008000', 'Зеленый'), ('#800080', 'Фиолетовый'), ('#FFFF00', 'Желтый')], default='#FF0000', help_text='Введите цвет тэга', image_field=None, max_length=18, samples=None, verbose_name='Цвет'),
        ),
    ]
