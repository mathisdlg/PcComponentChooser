from django.db import models

# Create your models here.
class Configuration(models.Model):
    def __str__(self):
        return f"{self.name} - {self.price}"

    name = models.CharField(max_length=100)
    notes = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Part(models.Model):
    def __str__(self):
        return f"{self.name} - {self.price}"
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)