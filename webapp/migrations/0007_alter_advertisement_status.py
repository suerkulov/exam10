# Generated by Django 4.0.5 on 2022-06-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_advertisement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('InModiration', 'На Модерацию'), ('Rejected', 'Отклонено'), ('Publiced', 'Опубликована')], default='На Модерацию', max_length=100, verbose_name='Статус'),
        ),
    ]
