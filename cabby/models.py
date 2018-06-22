from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver


import datetime as dt


from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as gis_models
from location_field.models.spatial import LocationField

from pyuploadcare.dj.models import ImageField






# ///////////////////////////////////////////////////////////////

class Rating(models.Model):
    user=models.OneToOneField(User)
    stars=models.IntegerField(max_length=5)
    review=models.CharField(max_length=255)

# ///////////////////////////////////////////////////////////////

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=User)
    def delete_user_profile(sender, instance, **kwargs):
        instance.profile.delete()
    
    @classmethod
    def all_user_details(cls):
        details = cls.objects.all()


    class Meta:
        ordering = ['user']


# ///////////////////////////////////////////////////////////////


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    production_year = models.DateField()
    licence_plate = models.CharField(max_length=7)

# ///////////////////////////////////////////////////////////////

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(max_length=10)
    national_id = models.IntegerField()
    car_type = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)



# ///////////////////////////////////////////////////////////////
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    # objects = gis_models.GeoManager()

# ///////////////////////////////////////////////////////////////
class DriverLocation(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    # objects = gis_models.GeoManager()