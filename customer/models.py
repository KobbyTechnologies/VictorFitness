from enum import _auto_null
from random import choices
from tabnanny import verbose
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import MyUser
from django_countries.fields import CountryField
from django.utils.safestring import mark_safe


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

    class Meta:
        verbose_name='Picture'

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.pic.url))

    photo.short_description = 'Image'
    photo.allow_tags = True
    
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

    

class PersonalPlan(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    highlight_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title


class PersonalPlanFeature(models.Model):
    sub_plan = models.ManyToManyField(PersonalPlan)
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title



class LifestyleInfo(models.Model):
    TIME_SPENT_ON = [
        ("Standing", "Standing"),
        ("Sitting", "Sitting"),
        ("Driving", "Driving"),
        ("Active", "Active"),
    ]
    occupation = models.CharField(max_length = 512, help_text = 'What do you do for a living?')
    work_hours = models.IntegerField(help_text="How many hours on average do you work each week?	")
    time_spent_on = models.CharField(choices=TIME_SPENT_ON, max_length=60, help_text = 'How do you spend the majority of your time at work?')
    shcedule = models.CharField(max_length = 512, help_text= 'Do you follow a regular working schedule, do you work days, afternoon or nights?')
    wake_up_status = models.CharField(max_length = 512, help_text = "When you wake up are you ")
    travel = models.CharField(max_length= 100, help_text = 'How often do you travel? ')
    body_weight_status = models.CharField(max_length = 100, help_text = "How would you consider your current body weight")
    activity_level = models.CharField(max_length = 100, help_text = "How would you describe your current activity level")
    job_stress_rating = models.IntegerField(help_text = 'How would you rate the stress of your job?')
    lifestyle_stress_rating = models.IntegerField(help_text = 'How would you rate the stress of your lifestyle?')
    physical_activities = models.TextField(help_text= 'Please list the physical activities that you participate in outside of the gym and outside of work.')
    reason_for_Lifestyle_change  = models.TextField(help_text = "Why have you decided to have a lifestyle review?")
    areas_to_focus_on = models.TextField(help_text="What is the main area that you would like to focus on?")


    class PhysicalActivityReadinessQuestionnaire(models.Model):
        heart_condition = models.BooleanField(help_text = 'Has your doctor ever said you have a heart condition? ')
        chest_pains = models.BooleanField(help_text= "Do you feel pain in your chest at rest, during your daily activities of living, or when you do physical activity?*")
        lost_consciousness_before = models.BooleanField(help_text = "Do you lose balance because of dizziness or have you lost consciousness in the last 12 months?*")
        other_medical_condition = models.BooleanField(help_text = "Have you ever been diagnosed with another chronic medical condition (other than heart disease or high blood pressure)?*")
        if_yes_explain = models.TextField(help_text = "If yes to the above question, please list the condition(s) here. ", blank = True)
        taking_prescribed_medicine = models.BooleanField(help_text= "Are you currently taking prescribed medications for a chronic medical condition?*")
        if_yes_list_medicine = models.TextField(help_text = "If yes to the previous question, please list your medications and how long you have been taking them. ", blank = True)























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
