from django.db import models

class Task(models.Model):
    title = models.CharField(max_length =128)
    image = models.FileField(upload_to ="tasks/images/")

  

    class Meta:
        db_table ="web_customer"
        ordering =["id"]

        
    def __str__ (self):
        return self.title




