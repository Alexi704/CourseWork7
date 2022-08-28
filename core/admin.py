from django.contrib import admin
from core.models import User


class UserAdmin(admin.ModelAdmin):
    # Вывод отображаемых полей в админке, в разделе "Пользователи":
    list_display = ('username', 'email', 'first_name', 'last_name')

    # Скрываем поля в админке
    exclude = ('password',)

    # Делаем поля неизменными(только для чтения):
    readonly_fields = ('last_login', 'date_joined')

    # Ставим фильтры (для сортировки пользователей):
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    # Организуем поиск, по заданным полям (поиск происходит сразу по всем указанным полям):
    search_fields = ('email', 'first_name', 'last_name', 'username')


admin.site.register(User, UserAdmin)
