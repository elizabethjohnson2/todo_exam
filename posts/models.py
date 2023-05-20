from django.db import models

class Task(models.Model):
    title = models.CharField(max_length =128)
    delete_image=models.FileField(upload_to="tasks/delete_image/",null=True,blank=True )
    edit_image=models.FileField(upload_to="tasks/edit_image/",null=True,blank=True  )
    is_delete = models.BooleanField(default=False)
    is_edit= models.BooleanField(default=False)
    


    def __str__ (self):
        return self.title

class Completed(models.Model):
    title = models.CharField(max_length =128)
    is_delete = models.BooleanField(default=False)
    is_edit= models.BooleanField(default=False)

     
    def __str__ (self):
        return self.title




