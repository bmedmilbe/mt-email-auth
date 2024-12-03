from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    nike = models.CharField(max_length=255, null=True, blank=True)

    CURRENCY_EUR = "EUR"
    CURRENCY_GBP = "GBP"
    CURRENCY_DBS = "DBS"
    CURRENCY_CHOICES = [
        (CURRENCY_EUR, CURRENCY_EUR),
        (CURRENCY_GBP, CURRENCY_GBP),
        (CURRENCY_DBS, CURRENCY_DBS),
    ]
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_EUR
    )
    value = models.DecimalField(max_digits=8, decimal_places=2, default=2)
    payment_day = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(31)],default=5)
    contact = models.CharField(max_length=15,unique=True)
    
    def __str__(self):
        return self.name

class Reference(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    referenced_by = models.ForeignKey(Person,on_delete=models.PROTECT, related_name="all_references")

class Payment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    prove = models.FileField(upload_to='camaramz/fund/proves/')
    date = models.DateField(auto_now=True)


class Trush(models.Model):
    date = models.DateField(auto_now=True)
    file = models.FileField(upload_to='camaramz/fund/contacts/', null=True)
    

    

    


