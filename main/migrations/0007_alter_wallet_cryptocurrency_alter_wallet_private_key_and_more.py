# Generated by Django 4.1.6 on 2023-02-15 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_wallet_cryptocurrency_alter_wallet_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='cryptocurrency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.token'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='private_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='public_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='telegram_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telegram_bot.telegramuser'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
