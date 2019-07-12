from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class InstaPost(models.Model):

    post_user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_image = models.ImageField(null=False,upload_to='PostImage')
    post_caption = models.CharField(max_length=50,null=False)
    post_location = models.CharField(max_length=50,null=True,blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    
    
    def get_absolute_url(self):
        return reverse('home')