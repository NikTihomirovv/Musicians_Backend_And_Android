from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Photo, Video, Audio


UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': (
        'about',
        'age',
        'vk_link',
        'tg_link',
        'rating',
        'city',
        'purpose',
        'instrument_1',
        'instrument_2',
        'instrument_3',
        'photo',
        'video',
        'audio',
    )}),
)
admin.site.register(MyUser, UserAdmin)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Audio)