# Generated by Django 4.2.2 on 2023-07-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0009_alter_exercisecollection_user_alter_unit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisecollection',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
