# Generated by Django 4.0.5 on 2022-06-25 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_advertisement_is_public_advertisement_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'permissions': [('staff', 'делает все')], 'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
    ]
