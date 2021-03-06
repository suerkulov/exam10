# Generated by Django 4.0.5 on 2022-06-25 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/', verbose_name='Фотография ')),
                ('caption', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('publicated_at', models.DateTimeField(auto_now=True, verbose_name='Время публикации')),
                ('is_public', models.BooleanField(default=False, verbose_name='Является ли публичными')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
                'db_table': 'advertisement',
            },
        ),
    ]
