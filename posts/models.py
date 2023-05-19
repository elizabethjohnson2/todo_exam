from django.db import models

class Task(models.Model):
    title = models.CharField(max_length =128)
    is_delete = models.BooleanField(default=False)
    is_edit= models.BooleanField(default=False)


    class Meta:
        db_table ="web_customer"
        ordering =["id"]

        
    def __str__ (self):
        return self.title




