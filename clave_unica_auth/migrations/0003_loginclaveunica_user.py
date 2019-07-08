# Generated by Django 2.2.2 on 2019-07-06 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clave_unica_auth', '0002_loginclaveunica_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginclaveunica',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]