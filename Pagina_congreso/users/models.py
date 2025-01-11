from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="avatares", blank=True, null=True, default="Avatar_default.jpg")
    
    def __str__(self):
        return f"{self.user} - {self.image}"