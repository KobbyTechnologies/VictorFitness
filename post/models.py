from tabnanny import verbose
from django.db import models
from authentication.models import MyUser
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from workouts.models import ProgramWorkout

# Create your models here.
STATUS = [
    (0, 'Draft'),
    (1, 'Published')
]


class Post(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField ('image')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0, help_text='Change to published to be enable viewing')
    workout = models.ForeignKey(ProgramWorkout, on_delete=models.PROTECT)
    author = models.ForeignKey(MyUser, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-date_created'] 
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


    @property
    def short_description(self):
        return truncatechars(self.content, 20)

    def post_photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    post_photo.short_description = 'Image'
    post_photo.allow_tags = True


    def __str__(self):
        return self.headline


