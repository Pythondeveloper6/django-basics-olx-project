from django.db import models

# Create your models here.


class Footer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("Footer")
        verbose_name_plural = ("Footers")

    def __str__(self):
        return self.name
