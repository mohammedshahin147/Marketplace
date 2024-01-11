from django.db import models
from authenticationapp.models import User , Profile
from sellerapp.models import Property

# Create your models here.

class Booking(models.Model):
    bookfor = models.ForeignKey(Property,on_delete=models.CASCADE)
    tenant = models.ForeignKey(User,on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    duration = models.IntegerField()
    total_rate = models.BigIntegerField()

    def __str__(self):
        return str(self.bookfor.property_name)
