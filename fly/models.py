from django.db import models

# Create your models here.

class Table(models.Model):

    file = models.FileField(upload_to='fly/flight')
    

    date = models.DateTimeField(auto_now=True, blank=True) 


class Country(models.Model):
    
    COUNTRY_CHOICES = [
        ("PT", "Portugal"),
        ("ST", "São Tomé e Príncipe"),
        ("BR", "Brasil"),
        ("GB", "Guiné-Bissau"),
        ("MZ", "Moçambique"),
        ("CV", "Cabo Verde"),
        ("AG", "Angola"),
    ]
    acronym = models.CharField(
        max_length=2, choices=COUNTRY_CHOICES, unique=True
    ) 
    name = models.CharField(max_length=255, unique=True)
    image = models.FileField(upload_to='fly/country/images/', null=True, blank=True)
  
    def __str__(self) -> str:
        return self.acronym

class Airport(models.Model):
    
    # COUNTRY_CHOICES = [
    #     ("PT", "Portugal"),
    #     ("ST", "São Tomé e Príncipe"),
    #     ("BR", "Brasil"),
    #     ("GB", "Guiné-Bissau"),
    #     ("MZ", "Moçambique"),
    #     ("CV", "Cabo Verde"),
    #     ("AG", "Angola"),
    # ]
    country = models.ForeignKey(Country,on_delete=models.PROTECT, null=True, related_name="airports") 

    acronym = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255, unique=True)   
    image = models.FileField(upload_to='fly/airport/images/', null=True, blank=True)

    


class Flight(models.Model):

    LIS_TMS = "LIS-TMS"
    TMS_LIS = "TMS-LIS"
    LIS_OXB = "LIS-OXB"
    OXB_LIS = "OXB-LIS"
    VPY_LIS = "VPY-LIS"
    LIS_VPY = "LIS-VPY"
    LAD_LIS = "LAD-LIS"
    LIS_LAD = "LIS-LAD"
    BSB_LIS = "BSB-LIS"
    LIS_BSB = "LIS-BSB"
    RAI_LIS = "RAI-LIS"
    LIS_RAI = "LIS-RAI"
    
    
    ROUTE_CHOICES = [
        (LIS_TMS, LIS_TMS),
        (TMS_LIS, TMS_LIS),
        (LIS_OXB,LIS_OXB),
        (OXB_LIS,OXB_LIS),
        (VPY_LIS, VPY_LIS),
        (LIS_VPY, LIS_VPY),
        (LAD_LIS, LAD_LIS),
        (LIS_LAD, LIS_LAD),
        (BSB_LIS, BSB_LIS),
        (LIS_BSB, LIS_BSB),
        (RAI_LIS, RAI_LIS),
        (LIS_RAI, LIS_RAI),
    ]


    date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    route = models.CharField(
        max_length=7, default=LIS_TMS, choices=ROUTE_CHOICES
    )
    
    def __str__(self) -> str:
        return f'{self.route} {self.date} {self.price}'
    
    class Meta():
        unique_together = ['date', 'route']

class Request(models.Model):

    date = models.DateTimeField(auto_now=True, blank=True) 
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="requests") 
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    obs = models.TextField(null=True, blank=True)



