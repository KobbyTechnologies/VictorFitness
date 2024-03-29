from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,username,password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")
        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,username,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_email_verified = True
        user.save(using=self._db)
        return user
    
class MyUser(AbstractBaseUser):
    email = models.EmailField( max_length=60, unique=True)
    username = models.CharField( max_length=200)
    first_name = models.CharField(max_length=60, blank=True)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    
    class  Meta: 
        verbose_name_plural  =  "Add User"
   
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']
     
    objects =  MyUserManager()

    def full_name(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
    

    full_name.short_description = 'Name'
    full_name.allow_tags = True
    
    def __str__(self):
        return str(self.username)
    
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
