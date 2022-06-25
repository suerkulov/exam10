from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'caption']
    list_filter = ['created_at']
    search_fields = ['caption']


admin.site.register(Advertisement, AdvertisementAdmin)
