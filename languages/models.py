from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Language(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title language')
    key = models.CharField(max_length=100, unique=True, verbose_name='Key language (ru, kg, en...)')
    image = models.ImageField(upload_to='images/', verbose_name="Image")
    description = models.TextField(verbose_name="Description", default='...')
    information = RichTextField(verbose_name='Information')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.title
