from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()
    
    def _str_(self):
        return self.city

# from django.db import models

# # Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     fees = models.IntegerField(null=True)
#     city = models.CharField(max_length=100)
#     roll = models.IntegerField()
    
#     def _str_(self):
#         return self.name

class ComStudent(models.Model):
        roll = models.CharField(max_length=100)
        name = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        fees = models.CharField(max_length=100)
        
        def _str_(self):
             return self.name