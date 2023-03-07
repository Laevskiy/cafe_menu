from django.db import models

# Create your models here.
class Category (models.Model):
    name_category = models.CharField(max_length= 255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    slug_category = models.SlugField (max_length=255)


class Dishes (models.Model):
    name_dishes = models.CharField(max_length= 255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    slug_dishes = models.SlugField(max_length=255)
    name_category = models.ForeignKey('Category', on_delete = models.PROTECT)

    def __str__(self):
        return self.name_dishes


class Ingredients(models.Model):
    name_ing = models.CharField (max_length=255)
    price_ing = models.IntegerField()

    def __str__(self):
        return self.name_ing


class Recept (models.Model):
    Dish = models.ForeignKey(Dishes,on_delete=models.CASCADE)
    Ingredients = models.ForeignKey(Ingredients,on_delete=models.CASCADE)
    kol = models.IntegerField ()

