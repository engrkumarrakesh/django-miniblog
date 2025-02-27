from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

  