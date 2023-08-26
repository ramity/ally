from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# class Brand(Base):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name}"

# class ServingUnit(Base):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name}"

# class Food(Base):
#     # ID
#     brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True)
#     # Serving
#     serving_size_amount = models.IntegerField()
#     serving_size_unit = models.ForeignKey(ServingUnit, on_delete=models.PROTECT)
#     serving_size_alt_amount = models.IntegerField()
#     serving_size_alt_unit = models.ForeignKey(ServingUnit, on_delete=models.PROTECT)
#     servings_per_container = models.IntegerField()
#     # Nutrition
#     calories = models.IntegerField()
#     total_fat = models.IntegerField(default=0)
#     saturated_fat = models.IntegerField(default=0)
#     trans_fat = models.IntegerField(default=0)
#     polyunsaturated_fat = models.IntegerField(default=0)
#     monounsaturated_fat = models.IntegerField(default=0)
#     cholesterol = models.IntegerField(default=0)
#     sodium = models.IntegerField(default=0)
#     total_carbohydrate = models.IntegerField(default=0)
#     total_sugars = models.IntegerField(default=0)
#     added_sugars = models.IntegerField(default=0)
#     protein = models.IntegerField(default=0)
#     # Vitamins and minerals
#     vitamin_A = models.IntegerField(default=0)
#     vitamin_C = models.IntegerField(default=0)
#     vitamin_D = models.IntegerField(default=0)
#     calcium = models.IntegerField(default=0)
#     iron = models.IntegerField(default=0)
#     potassium = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.brand} {self.name} - {self.calories}"

# class FoodEntry(Base):
#     serving_count = models.IntegerField()
#     # weight = 
#     # meal_time = 

# class Meal(Base):
#     foods = models.ManyToManyField(Food)

# class MealEntry(Base):
#     pass

