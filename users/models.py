from django.db import models


class User (models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)
    division = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email =models.EmailField()
    password = models.CharField(max_length=128)

    def __str__ (self):
         return self.title
       

