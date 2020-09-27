from django.contrib import admin

# Register your models here.
from dappx.models import UserProfileInfo, User, Post, JsonFile
# Register your models here.
admin.site.register([UserProfileInfo, Post, JsonFile])