from datetime import datetime
from tabnanny import verbose
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import MyUser

#Name, Contacts, Gender, Weight, Height, Date of birth, Start date , Photos, Goals

# Create your models here.

class UserInfo(models.Model):
    GENDER=[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
         ]
    names=models.OneToOneField(MyUser,on_delete=models.CASCADE )
    contacts=models.CharField(max_length=30, verbose_name="Contact", blank=True)
    gender=models.CharField(choices=GENDER, max_length=30,blank=True, verbose_name="Gender")
    weight=models.CharField(max_length=30, verbose_name="Weight(kgs)", blank=True)
    height=models.CharField(max_length=30,verbose_name="Height(ft)", blank=True)
    date_of_birth=models.DateField(verbose_name="Date of Birth", blank=True)
    photos=CloudinaryField("image" ,blank=True)
    goals=models.TextField(verbose_name="Goals", blank=True)
    start_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="User Profile"


    def __str__(self):
        return self.contacts
    
    
    

    


