# Generated by Django 5.0.1 on 2024-01-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_learnedtext_learnedword'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnedtext',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='learnedword',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]