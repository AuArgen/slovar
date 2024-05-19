from django.db import models
from ckeditor.fields import RichTextField
from languages.models import Language


# Create your models here.
class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/lessons')
    description = RichTextField()
    show = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title


class EventTest(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/lessons')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'event test'
        verbose_name_plural = 'event tests'

    def __str__(self):
        return self.title


class Tests(models.Model):
    eventTest = models.ForeignKey(EventTest, on_delete=models.CASCADE)
    question = RichTextField(verbose_name='question')
    a = RichTextField(verbose_name='a варият')
    b = RichTextField(verbose_name='б варият')
    c = RichTextField(verbose_name='в варият')
    d = RichTextField(verbose_name='г варият')
    answer = models.CharField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question



class Game(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    title = models.CharField(max_length=255, verbose_name='Вопрос')
    question = models.TextField(verbose_name='Ответ')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.title