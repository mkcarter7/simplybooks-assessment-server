from django.db import models

class Author(models.Model):
  
  email = models.CharField(max_length=50)
  favorite = models.BooleanField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  image = models.URLField()
  uid = models.CharField(max_length=30)
