from django.db import models

# Create your models here.
class Restaurent(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=3, max_digits=7)
    longitude = models.DecimalField(decimal_places=3, max_digits=7)
    picture = models.CharField(default="None", max_length=500)
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField()
    restaurent = models.ForeignKey(Restaurent, related_name='dishes', on_delete=models.CASCADE)


class History(models.Model):
    user = models.TextField()

class Order(models.Model):
    cost = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    dishes = models.ManyToManyField(Dish)
    restaurent = models.ForeignKey(Restaurent, on_delete=models.DO_NOTHING)
    history = models.ForeignKey(History, on_delete=models.CASCADE)


