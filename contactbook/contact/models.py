from django.db import models

# Create your models here.

class registerView(models.Model):
    username = models.CharField(max_length=65)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    password = models.CharField(max_length=65)
    
    def __str__(self):
        return self.username