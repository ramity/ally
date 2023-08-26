from django.contrib import admin
from .models import *

admin.site.register(Muscle)
admin.site.register(Unit)
admin.site.register(Exercise)
admin.site.register(ExerciseEntry)
admin.site.register(ExerciseLog)
admin.site.register(ExerciseCollection)
admin.site.register(ExerciseSplit)
admin.site.register(ExerciseSplitCollection)
