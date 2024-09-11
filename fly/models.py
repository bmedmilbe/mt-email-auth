from django.db import models

# Create your models here.


    

class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}' 
    

class Trush(models.Model):
    date = models.DateField(auto_now=True)
    file = models.FileField(upload_to='marvoa/prices', null=True)
    text = models.TextField(null=True)
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name="city_from_trush")
    city_to = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name="city_to_trush")


class Airline(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.name}' 


class Flight(models.Model):
    
    date = models.DateTimeField() 
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name="city")
    city_to =  models.ForeignKey(City, on_delete=models.CASCADE,  null=True, blank=True, related_name="city_to")
    base_price = models.IntegerField(blank=True, null=True) 
    final_price = models.IntegerField(blank=True, null=True) 
    airline =  models.ForeignKey(Airline, on_delete=models.CASCADE,  null=True, blank=True, related_name="arlines")
    
    class Meta():
        unique_together = ['airline', 'date', 'city', 'final_price']
    
    def __str__(self):
        return f"{self.airline.name} {self.date} {self.final_price}"

class Enquire(models.Model):
    contact = models.CharField(max_length=255, null=True, blank=True)
    date =models.DateTimeField(auto_now=True, blank=True, null=True) 
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True, related_name="flights")
    STATUS_TALKED = "T"
    STATUS_PENDENT = "P"
    STATUS_COMPLETED = "D"
    STATUS_CHOICES = [
        (STATUS_TALKED, "Talked"),
        (STATUS_PENDENT, "Pendent"),
        (STATUS_COMPLETED, "Completed"),
    ]

    status = models.CharField(
        max_length=1, default=STATUS_PENDENT, choices=STATUS_CHOICES
    )
    def __str__(self) -> str:
        return f'{self.contact}' 
    


# class Users(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     def __str__(self) -> str:
#         return f'{self.name}' 

# class Moviments(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=True, related_name="users")
#     value = models.IntegerField(blank=True, null=True) 
#     date = models.DateTimeField(auto_now=True, blank=True, null=True) 
#     description = models.CharField(max_length=255, null=True, blank=True)
#     TYPE_IN = "IN"
#     TYPE_OUT = "OUT"
    
#     TYPE_CHOICES = [
#         (TYPE_IN, "Received"),
#         (TYPE_OUT, "Gave"),
#     ]

#     type = models.CharField( max_length=3, choices=TYPE_CHOICES)

class Menssenger(models.Model):
    file = models.FileField(upload_to='exchange/balances', null=True)
    details = models.TextField(blank=True, null=True)
    
    





