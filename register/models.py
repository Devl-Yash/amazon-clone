from django.db import models

# Create your models here.
class dislogin(models.Model):
    GENDER_CHOICE = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]

    Name = models.CharField(max_length = 100)
    Gender = models.CharField(choices = GENDER_CHOICE, default = None)
    ContactNo = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    Pincode = models.IntegerField()

