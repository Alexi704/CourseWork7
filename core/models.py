from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractUser):
    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя',
        help_text='Введите имя (максимум 64 символа).',
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия',
        help_text='Введите фамилию (максимум 64 символа).',
    )
    email = models.EmailField(
        'email address',
        unique=True,
        help_text='Укажите электронную почту.',
    )
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name='Роль пользователя',
        help_text='Выбирите роль пользователя.',
    )
    is_active = models.BooleanField(
        verbose_name='Статус активности аккаунта',
        help_text='Укажите, активен ли аккаунт.',
    )
    image = models.ImageField(
        upload_to='users_avatars/',
        verbose_name='Аватарка',
        help_text='Выбирите свой аватар',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
