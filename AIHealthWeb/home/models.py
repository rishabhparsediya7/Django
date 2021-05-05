from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    contact=models.CharField(max_length=122)
    password=models.CharField(max_length=122)

