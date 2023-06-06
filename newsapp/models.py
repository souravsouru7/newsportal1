from django.db import models
from django.utils import timezone

# Create your models here.
class news(models.Model):
   
    text=models.TextField()
    photos=models.ImageField(upload_to='photos/')
    headline=models.CharField(max_length=1000,default="coming soon")
    date_field = models.DateField(default=timezone.now)
   
    def __str__(self):
        return self.headline
    