from ckeditor.fields import RichTextField
from django.db import models

from languages.models import Language


# Create your models here.

class Teacher(models.Model):
    fio = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers/')
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    information = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.fio


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    information = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title