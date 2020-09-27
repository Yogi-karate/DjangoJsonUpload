
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class Post(models.Model):
     title = models.CharField(max_length=120)
     body = models.TextField()
     user_id = models.CharField(max_length=3)
     def __str__(self):
        return self.title
class JsonFile(models.Model):
     file = models.FileField(validators=[validate_file_extension])