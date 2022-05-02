from datetime import datetime
from tabnanny import verbose
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import MyUser


class UserInfo(models.Model):
    GENDER=[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
         ]
    names=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    contacts=models.CharField(max_length=30, verbose_name="Contact", blank=True)
    gender=models.CharField(choices=GENDER, max_length=30,blank=True, verbose_name="Gender")
    date_of_birth=models.DateField(verbose_name="Date of Birth", blank=True)
    start_date=models.DateTimeField(auto_now_add=True)
    profilePic = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name_plural="User Profile"
        constraints = [models.UniqueConstraint(fields=["names"], name="unique_case")]

    def __str__(self):
        return self.contacts
    
class Gallery(models.Model):
    pic=  CloudinaryField("image" ,blank=True) 
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE) 
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Workout(models.Model):
    weight = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(blank=True,max_length=100)
    bmi = models.IntegerField(blank=True,default=0.0)
    recommendations = models.TextField(blank=True)
    waist = models.IntegerField(blank=True,default=0.0)
    hip = models.IntegerField(blank=True,default=0.0)
    whr = models.IntegerField(blank=True,default=0.0)
    whrStatus = models.CharField(blank=True,max_length=100)
    
class Goals(models.Model):
    goals = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)

