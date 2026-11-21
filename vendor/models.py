from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'image/')
    price = models.IntegerField()
    
