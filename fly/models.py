from django.db import models

# Create your models here.


class Contact(models.Model):
    contact = models.CharField(max_length=255, null=True, blank=True)

class Enquire(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now=True, blank=True) 
    country = models.CharField(max_length=255)
    depart_date =   models.DateField() 
    return_date =   models.DateField(blank=True, null=True) 
    base_price = models.DecimalField(decimal_places=2, max_digits=8,blank=True, null=True) 
    final_price = models.DecimalField(decimal_places=2, max_digits=8,blank=True, null=True) 
    paid = models.BooleanField(default=False)
    obs = models.TextField(null=True, blank=True)





