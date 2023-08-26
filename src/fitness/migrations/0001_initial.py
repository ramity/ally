# Generated by Django 4.2.2 on 2023-07-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitness.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('abbr', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('exercises', models.ManyToManyField(blank=True, to='fitness.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('entries', models.ManyToManyField(to='fitness.exerciseentry')),
            ],
        ),
        migrations.AddField(
            model_name='exerciseentry',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitness.unit'),
        ),
        migrations.CreateModel(
            name='ExerciseCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs', models.ManyToManyField(to='fitness.exerciselog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscles',
            field=models.ManyToManyField(to='fitness.muscle'),
        ),
    ]