from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Program(models.Model):
    Program_Type = models.CharField(max_length=600)
    
    def __str__(self):
        return str(self.Program_Type)
class Program_Detail(models.Model):
    LEVEL = [
        ('Beginner','Beginner'),
        ('Intermidiate','Intermidiate'),
        ('Pro','Pro'),
        ('All Levels','All Levels'),
    ]
    STATUS = [
        ('Free','Free'),
        ('Paid','Paid'),
    ]
    Program_Name = models.ForeignKey(Program, on_delete=models.CASCADE,related_name="programs")
    title = models.CharField(max_length=600)
    description = models.TextField()
    level = models.CharField(choices=LEVEL,max_length=255, blank=True)
    status = models.CharField(choices=STATUS,max_length=255, blank=True)
    image = CloudinaryField('image', blank=True)
    price = models.IntegerField(blank=True,null=True) 
    last_update = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return str(self.title)
    
class Topic(models.Model):
    video = CloudinaryField(blank=True)
    video_title = models.CharField(max_length=1000,blank=True)
    description = models.TextField()
    program=models.ForeignKey(Program_Detail,on_delete=models.CASCADE,related_name="videos")
    last_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.video_title)
    
class ProgramAttachments(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=1000,blank=True)
    program=models.ForeignKey(Program_Detail,on_delete=models.CASCADE,related_name="files")
    last_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_name)
    