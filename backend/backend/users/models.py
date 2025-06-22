from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from constants import (
    RATING_CHOICES,
    MIN_AGE, MAX_AGE,
    CITY_CHOICES,
    PURPOSE_CHOICES,
    INSTRUMENT_CHOICES,
    CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
    ABOUT_MAX_LENGHT
)


class MyUser(AbstractUser):
    '''Модель пользователяю.'''

    about = models.TextField(
        verbose_name='О себе',
        help_text='Заполните информацию в блоке',
        blank=True,
        null=True,
        max_length=ABOUT_MAX_LENGHT)
    age = models.SmallIntegerField(
        verbose_name='Возраст',
        help_text='Заполните информацию в блоке',
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                MIN_AGE,
                f'Минимальное значение - {MIN_AGE}'
            ),
            MaxValueValidator(
                MAX_AGE,
                f'Максималое значение - {MAX_AGE}'
            )
        ]
    )
    vk_link = models.URLField(
        verbose_name='Ссылка на профиль в ВК',
        help_text='Заполните информацию в блоке',
        blank=True,
        null=True,
    )
    tg_link = models.URLField(
        verbose_name='Ссылка на профиль в ТГ',
        help_text='Заполните информацию в блоке',
        blank=True,
        null=True,
    )
    rating = models.SmallIntegerField(
        verbose_name='Рейтинг',
        help_text='Заполните информацию в блоке',
        blank=True,
        null=True,
        choices=RATING_CHOICES,
    )
    city = models.CharField(
        verbose_name='Город',
        help_text='Заполните информацию в блоке',
        max_length=CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        choices=CITY_CHOICES,
    )
    purpose = models.CharField(
        verbose_name='Цель',
        help_text='Заполните информацию в блоке',
        max_length=CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        choices=PURPOSE_CHOICES,
    )
    instrument_1 = models.CharField(
        verbose_name='Инструмент 1',
        help_text='Заполните информацию в блоке',
        max_length=CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        choices=INSTRUMENT_CHOICES,
    )
    instrument_2 = models.CharField(
        verbose_name='Инструмент 2',
        help_text='Заполните информацию в блоке',
        max_length=CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        choices=INSTRUMENT_CHOICES,
    )
    instrument_3 = models.CharField(
        verbose_name='Инструмент 3',
        help_text='Заполните информацию в блоке',
        max_length=CITY_PURPOSE_INSTRUMENT_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        choices=INSTRUMENT_CHOICES,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        help_text='Заполните информацию в блоке',
        upload_to='users_avatars',
    )
    photo = models.ManyToManyField(
        'Photo',
        verbose_name='Фотография',
        help_text='Заполните информацию в блоке',
        blank=True,
    )
    video = models.ManyToManyField(
        'Video',
        verbose_name='Видеозапись',
        help_text='Заполните информацию в блоке',
        blank=True,
    )
    audio = models.ManyToManyField(
        'Audio',
        verbose_name='Аудиозапись',
        help_text='Заполните информацию в блоке',
        blank=True,
    )

    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Photo(models.Model):
    '''Модель фотографий.'''

    photo = models.ImageField(
        upload_to='users_photo',
    )
    
    class Meta: 
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
    

class Video(models.Model):
    '''Модель видео.'''

    video = models.FileField(
        upload_to='users_video',
    )
    
    class Meta: 
        verbose_name = 'Видеозапись'
        verbose_name_plural = 'Видеозаписи'
    

class Audio(models.Model):
    '''Модель аудио.'''

    audio = models.FileField(
        upload_to='users_audio',
    )
    
    class Meta: 
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'
