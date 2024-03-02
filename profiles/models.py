from django.db import models

# Create your models here.

# For files
# class UserProfile(models.Model):
#     image = models.FileField(upload_to="images")

# Image field
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
