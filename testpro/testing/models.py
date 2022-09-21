from django.db import models

# Create your models here.
# outer models
class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# inner models
class Package(models.Model):
    id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey("Subcategory", on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    partial = models.IntegerField()
    capacity = models.IntegerField()
    def __str__(self):
        return str(self.id)

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey("Package", on_delete=models.CASCADE)
    city= models.ForeignKey("City", on_delete=models.CASCADE)
    area = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return str(self.id)


class Constraints(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey("Package", on_delete=models.CASCADE)
    upper_limit = models.IntegerField()
    def __str__(self):
        return str(self.id)




    