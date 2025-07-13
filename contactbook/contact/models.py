from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    person_name = models.CharField(_("person name"),max_length=100)
    email = models.EmailField(_("email"), max_length=254)
    phone_number = models.CharField(_("Mobile number"), max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(_("image"), upload_to='contact_images/')
    label = models.CharField(_("label"), max_length=100)
    last_updated = models.DateTimeField(_("last updated"), auto_now=True)
    created_at = models.DateTimeField(_("Created"),auto_now=True)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.id} - {self.person_name}'
     
    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})

