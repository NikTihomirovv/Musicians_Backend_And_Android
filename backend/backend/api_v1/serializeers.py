from rest_framework import serializers
from django.core.files.base import ContentFile
from users.models import MyUser
import base64


class Base64ImageField(serializers.ImageField):
    """Кодирует фото в BASE64."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')  
            ext = format.split('/')[-1]  
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class IndexSerializer(serializers.ModelSerializer):
    """Возвращает список пользователей."""

    avatar = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'instrument_1',
            'instrument_2',
            'instrument_3',
            'purpose',
            'city'
        )
        model = MyUser
