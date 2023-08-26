# Generated by Django 4.2.2 on 2023-07-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='muscles',
        ),
        migrations.RemoveField(
            model_name='muscle',
            name='exercises',
        ),
        migrations.AddField(
            model_name='exercise',
            name='main_muscles',
            field=models.ManyToManyField(related_name='main_exercises', to='fitness.muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='stabilizing_muscles',
            field=models.ManyToManyField(related_name='stablizing_exercises', to='fitness.muscle'),
        ),
    ]