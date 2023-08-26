from django.db import models
from django.contrib.auth.models import User

class Muscle(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return f"{self.name}"

class Unit(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    abbr = models.CharField(max_length = 16)

    def __str__(self):
        return f"{self.abbr}"

class Exercise(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    primary_muscles = models.ManyToManyField(Muscle, related_name='primary_exercises')
    secondary_muscles = models.ManyToManyField(Muscle, related_name='secondary_exercises')
    stabilizing_muscles = models.ManyToManyField(Muscle, related_name='stabilizing_exercises')
    rack_safety_index = models.IntegerField(blank=True, null=True)
    rack_cup_index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class ExerciseEntry(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete = models.PROTECT)
    weight = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete = models.PROTECT)
    reps = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        year = self.created_at.year
        month = self.created_at.month
        day = self.created_at.day
        hour = self.created_at.hour
        minute = self.created_at.minute
        date_string = f"{year}/{month}/{day}@{hour}:{minute}"
        return f"{date_string} - {self.exercise} @{self.weight}{self.unit} x {self.reps} ({self.weight * self.reps} { self.unit }*rep)"

class ExerciseLog(models.Model):
    entries = models.ManyToManyField(ExerciseEntry)
    day = models.DateField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.day}"

class ExerciseCollection(models.Model):
    logs = models.ManyToManyField(ExerciseLog)
    user = models.OneToOneField(User, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.user}"

class ExerciseSplit(models.Model):
    name = models.CharField(max_length = 255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.name}"

class ExerciseSplitCollection(models.Model):
    name = models.CharField(max_length = 255)
    splits = models.ManyToManyField(ExerciseSplit)
    user = models.OneToOneField(User, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.name}"
