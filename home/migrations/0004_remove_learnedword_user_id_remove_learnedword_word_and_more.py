# Generated by Django 5.0.6 on 2024-05-19 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_learnedtext_active_learnedword_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learnedword',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='learnedword',
            name='word',
        ),
        migrations.RemoveField(
            model_name='text',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='word',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='LearnedText',
        ),
        migrations.DeleteModel(
            name='LearnedWord',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
