from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Movies(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='movie_image')
    trailer=models.FileField(upload_to=None, max_length=500)
    options=(
        ('Malayalam','Malayalam'),
        ('Tamil','Tamil'),
        ('Hindi','Hindi')
    )
    category=models.CharField(max_length=200,choices=options,default='Malayalam')
    description=models.CharField(max_length=500,null=True,)
    rating=models.FloatField(default='5')
    cast1=models.ImageField(null=True,upload_to='movie_image')
    cast2=models.ImageField(null=True)
    cast3=models.ImageField(null=True)
    cast4=models.ImageField(null=True)
    cast5=models.ImageField(null=True)
    

    
class Theaters(models.Model):
    movies=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    show=models.TimeField()
    adress=models.CharField(max_length=500)
    price=models.IntegerField(null=True)

    
class Books(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    theater=models.ForeignKey(Theaters,on_delete=models.CASCADE,related_name='theaterbook')
    phone=models.IntegerField()
    show=models.TimeField(auto_now=False, auto_now_add=False)
    seat=models.IntegerField(null=True)
    date=models.DateField(null=True)
    options=(
        ('Booking Confirmed','Booking Confirmed'),
        ('Cancelled','Cancelled'),
    )
    status=models.CharField(max_length=100,choices=options,default='Booking confirmed')      
    
    @property
    def totalamnt(self):
        return self.theater.price*self.seat 
    
    def get_absolute_url(self):
        return reverse('bookings')