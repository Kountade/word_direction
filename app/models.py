from django.db import models

# Create your models here.

class blog(models.Model):
    category = models.CharField(max_length=5000)
    title = models.CharField(max_length=5000)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
