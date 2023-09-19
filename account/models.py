from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.


# class Movies(models.Model):
#     name=models.CharField(max_length=100)
#     image=models.ImageField(upload_to='movie_image')
#     trailer=models.FileField(upload_to=None, max_length=500)
#     options=(
#         ('Mlayalam','Malayalam'),
#         ('Tamil','Tamil'),
#         ('Hindi','Hindi')
#     )
#     category=models.CharField(max_length=200,choices=options,default='Malayalam')
#     description=models.CharField(max_length=500,null=True,)
#     rating=models.IntegerField(default='5')
#     cast=models.ImageField(null=True)

    
# class Theaters(models.Model):
#     name=models.CharField(max_length=100)
#     show=models.TimeField()
#     adress=models.CharField(max_length=500)

    
# class Books(models.Model):
#     movie=models.ForeignKey(Movies,on_delete=models.CASCADE)    
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     theater=models.ForeignKey(Theaters,on_delete=models.CASCADE,related_name='theaterbook')
#     phone=models.IntegerField()
#     show=models.TimeField(auto_now=False, auto_now_add=False)
#     options=(
#         ('Booking Confirmed','Booking Confirmed'),
#         ('Cancelled','Cancelled'),
#     )
#     status=models.CharField(max_length=100,choices=options,default='Booking confirmed')       