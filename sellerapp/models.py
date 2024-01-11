from django.db import models
from django.utils import timezone


# Create your models here.

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    rate = models.IntegerField()
    rented = models.BooleanField(default=False)
    available_from = models.DateField(default=timezone.now) 
    description = models.TextField(blank=True)

    RATE_CHOICES = [

        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
        ('600', '600'),
        ('700', '700'),
        ('800', '800'),
        ('900', '900'),
        ('1000', '1000'),
        ('2000', '2000'),
        ('3000', '3000'),
        ('4000', '5000'),
        ('6000', '6000'),
        ('7000', '7000'),
        ('8000', '8000'),
        ('9000', '9000'),
        ('10000', '10000'),
        ('15000', '15000'),
        
    ]

    rate = models.CharField(choices=RATE_CHOICES)

    CATEGORY_CHOICES = [
        ('1BHK', '1 Bedroom, Hall, Kitchen, 1 Car Parking'),
        ('2BHK', '2 Bedrooms, Hall, Kitchen, 1 Car Parking'),
        ('3BHK', '3 Bedrooms, 2 Hall, Kitchen, 2 Car Parking'),
        ('4BHK', '4 Bedrooms, 2 Hall, 2 Kitchen, 3 Car Parking'),
        ('5BHK', '5 Bedrooms, 2 Hall, 2 Kitchen, 4 Car Parking'),
    ]

    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    
    LOCATION_CHOICES = [
    ('trivandrum ', 'trivandrum city , nedumangad , kazhakkoottam ,attingal'),
    ('kollam', 'kollam , ayoor , anchal , kadakkal'), 
    ('Alappuzha', 'cherthala , harippad , mavelikkara , kayamkulam , ambalapuzha, aroor '),
    ('ernakulam', 'kochi , paravur , aluva , kanayannor , muvattupuzha , kothamangalam '),
    ('kozhikode', 'calicut ,vatakara , koyilandy , thamarassery '),
    ('kasargod', 'kasargod , hosdurg , vellarikkund , manajeshwaram '),
    ('idukki', 'idukki, devikulam , udumbanchola , thodupuzha , peerumade'),
    ]

    location = models.CharField(choices=LOCATION_CHOICES)


    def __str__(self):
        return str(self.property_name)


