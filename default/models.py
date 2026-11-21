from django.db import models

# Create your models here.
class vendorlogin(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    area = models.IntegerField()
    contactno = models.IntegerField()
    email = models.EmailField()


