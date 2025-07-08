from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
 
class ChaiVarity(models.Model):
     CHAI_TYPES_CHOICE = [
         ('Masala', 'Masala Chai'),
         ('Ginger', 'Ginger Chai'),
         ('Cardamom', 'Cardamom Chai'),
         ('Lemon', 'Lemon Chai'),
         ('Plain', 'Plain Chai'),
     ]
     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to='chais/')
     date_added = models.DateTimeField(default=timezone.now)
     type = models.CharField(max_length=20, choices=CHAI_TYPES_CHOICE, default='Plain')
     description = models.TextField(default="", blank=True)
     price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

     def __str__(self):
         return self.name
     
# One to Many relationship with User

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username}'s review of {self.chai.name}"
    
# Many to Many relationship with User
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')
    
    def __str__(self):
        return f"Store: {self.name}, Location: {self.location}"
    
# One to One relationship with User
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()
    
    def __str__(self):
        return f"Chai Certificate for {self.chai.name}, Certificate No: {self.certificate_number}"

