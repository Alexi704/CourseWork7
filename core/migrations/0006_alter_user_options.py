# Generated by Django 4.1 on 2022-08-31 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={
                'ordering': ['id'],
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
