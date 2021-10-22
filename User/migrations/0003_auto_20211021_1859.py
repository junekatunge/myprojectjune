# Generated by Django 3.2.8 on 2021-10-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]
