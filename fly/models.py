from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}' 


class Contact(models.Model):
    contact = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.contact}' 

class Enquire(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now=True, blank=True) 
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name="countries")
    country_to =  models.ForeignKey(Country, on_delete=models.CASCADE,  null=True, blank=True, related_name="countries_to")
    depart_date =   models.DateField() 
    return_date =   models.DateField(blank=True, null=True) 
    base_price = models.DecimalField(decimal_places=2, max_digits=8,blank=True, null=True) 
    final_price = models.DecimalField(decimal_places=2, max_digits=8,blank=True, null=True) 
    paid = models.BooleanField(default=False)
    obs = models.TextField(null=True, blank=True)
    done =  models.BooleanField(default=False)





