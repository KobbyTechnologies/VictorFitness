from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import MyUser
from django_countries.fields import CountryField


class UserInfo(models.Model):
    GENDER=[
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
         ]
    names=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    contacts=models.CharField(max_length=30, verbose_name="Contact", blank=True,null=True)
    gender=models.CharField(choices=GENDER, max_length=30,blank=True, verbose_name="Gender",null=True)
    date_of_birth=models.DateField(verbose_name="Date of Birth", blank=True,null=True)
    start_date=models.DateTimeField(auto_now_add=True)
    profilePic = models.ImageField(upload_to='img/',default='1.png')

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
    bmi = models.FloatField(blank=True,default=0.0)
    recommendations = models.TextField(blank=True)
    waist = models.IntegerField(blank=True,default=0.0)
    hip = models.IntegerField(blank=True,default=0.0)
    whr = models.FloatField(blank=True,default=0.0)
    whrStatus = models.CharField(blank=True,max_length=100)
    
class Goals(models.Model):
    goals = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    


class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    highlight_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title


class SubscriptionFeatures(models.Model):
    sub_plan = models.ManyToManyField(SubscriptionPlan)
    title = models.CharField(max_length=255)

    class Meta: 
        verbose_name = 'Subscription Plan Feature'
        verbose_name_plural = 'Subscription Plan Features'

    def __str__(self):
        return self.title


















class FullInfo(models.Model):
    GENDER = [
        ('Male','male'),
        ('Female', 'Female'),
        ("Other", "Other")
    ]

    GOAL = [
        ('Weight Loss' , 'Weight Loss'),
        ('Strength' , 'Strength'),
        ('Conditioning' , 'Conditioning'),
        ('Muscle Gain' , 'Muscle Gain'),
        ('Stay Fit' , 'Stay Fit'),
        ('Mobility & Flexibility' , 'Mobility & Flexibility'),
        ('Nutrition/Diet' , 'Nutrition/Diet'),
        ('Other' , 'Other')
    ]

    FITNESS_LEVEL = [
        ('Beginner' , 'Beginner'),
        ('Intermediate' , 'Intermediate'),
        ('Advanced' , 'Advanced'),
        ('Athlete' , 'Athlete')
    ]

    SESSIONS = [
        (1 , 1),
        (2 , 2),
        (3 , 3),
        (4 , 4),
        (5 , 5),
        (6 , 6),
        (7 , 7)
    ]
    PROGRAM = [
        ('Bodybuilding', 'Bodybuilding'),
        ('Weight Lose', 'Weight Lose'),
        ('Conditioning', 'Conditioning'),
        ('Strength', 'Strength'),
        ('Full Body', 'Full Body'),
        ('Metcon', 'Metcon'),
        ('Circuit', 'Circuit'),
        ('Tabata', 'Tabata'),
        ('Mobility & Flexibility', 'Mobility & Flexibility')

    ]
    
    # stage 1 Fields
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    adress_line_1 = models.CharField(max_length=50, blank=True)
    adress_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=200)
    country = CountryField(blank_label = '(select Country)')
    phone = models.CharField(max_length=32)
    gender = models.CharField(max_length=25, choices=GENDER)

    # stage 2 Fields
    goal = models.CharField(max_length=50, choices=GOAL)
    fitness_level = models.CharField(max_length=50, choices=FITNESS_LEVEL)
    number_of_sessions = models.IntegerField(choices=SESSIONS)
    program = models.CharField(max_length=50, choices=PROGRAM)
    personal_coach = models.BooleanField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
