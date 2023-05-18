from django.db import models

class Task(models.Model):
    title = models.CharField(max_length =128)


    class Meta:
        db_table ="web_customer"
        ordering =["id"]

        
    def __str__ (self):
        return self.title




