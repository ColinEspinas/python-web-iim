from django.db import models

# Create your models here.
class Messages(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  text=models.CharField(max_length=200)