# Generated by Django 4.0.5 on 2022-06-21 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tikets', '0005_remove_tikets_tikets_owner_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tikets',
            name='tikets_Owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
