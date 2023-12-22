from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=50) # validate max_length again if you want
    review_text = models.TextField()  
    rating = models.IntegerField()