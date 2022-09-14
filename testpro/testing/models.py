from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    name =  models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    