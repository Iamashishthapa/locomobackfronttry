from django.db import models

# Create your models here.
class Ashish(models.Model):
    title= models.TextField(default="ashish")
    discription= models.TextField(default="ashish")

    def __str__(self):
        return self.title