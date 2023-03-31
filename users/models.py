from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from ckeditor.fields import RichTextField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    membership = models.IntegerField(default=0)
    email2 = models.EmailField(max_length=100, blank=True)
    emial3 = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    mobile = models.CharField(max_length=14, blank=True)
    mobile2 = models.CharField(max_length=14, blank=True)
    designation = models.CharField(max_length=100, blank=True)


    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    nid = models.CharField(max_length=10, blank=True)
    birth_certificate = models.CharField(max_length=30, blank=True)

    # email_token = models.CharField(max_length=200, blank=True)
    # is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class AdditionalFields(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    fieldname = models.CharField(max_length=100, blank=True)
    value = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.profile.username
    
