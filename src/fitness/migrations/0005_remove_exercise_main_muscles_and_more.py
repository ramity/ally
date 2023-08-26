# Generated by Django 4.2.2 on 2023-07-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_rename_time_exerciseentry_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='main_muscles',
        ),
        migrations.AddField(
            model_name='exercise',
            name='primary_muscles',
            field=models.ManyToManyField(related_name='primary_exercises', to='fitness.muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_muscles',
            field=models.ManyToManyField(related_name='secondary_exercises', to='fitness.muscle'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='stabilizing_muscles',
            field=models.ManyToManyField(related_name='stabilizing_exercises', to='fitness.muscle'),
        ),
    ]