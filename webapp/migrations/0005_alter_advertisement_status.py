# Generated by Django 4.0.5 on 2022-06-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_advertisement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('На Модерацию', 'На Модерацию'), ('Отклонено', 'Отклонено'), ('Опубликована', 'Опубликована')], default=('На Модерацию', 'На Модерацию'), max_length=100, verbose_name='Статус'),
        ),
    ]
