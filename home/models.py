from django.db import models
from accounts.models import CustomUser


class Word(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translate = models.CharField(max_length=100)
    create = models.DateTimeField()

    class Meta:
        verbose_name = 'word'
        verbose_name_plural = 'Words'

    def __str__(self):
        return str(self.word)


class Text(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.CharField(max_length=500)
    translate = models.CharField(max_length=500)
    create = models.DateTimeField()

    class Meta:
        verbose_name = 'text'
        verbose_name_plural = 'Texts'

    def __str__(self):
        return str(self.word)


class LearnedWord(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


class LearnedText(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.ForeignKey(Text, on_delete=models.CASCADE)
