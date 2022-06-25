from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Advertisement(models.Model):
    photo = models.ImageField(verbose_name="Фотография ", upload_to="photos/", null=False, blank=False)
    caption = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Текст')
    price = models.IntegerField(verbose_name='Цена', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    last_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    publicated_at = models.DateTimeField(auto_now=True, verbose_name="Время публикации")

    author = models.ForeignKey(
        User,
        related_name="advertisements",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    is_public = models.BooleanField(verbose_name='Является ли публичными', default=False)

    def __str__(self):
        return f"{self.pk}. {self.caption}: {self.text}"

    class Meta:
        db_table = 'advertisement'
        verbose_name = 'Обьявление'
        verbose_name_plural = "Обьявления"