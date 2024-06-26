# Generated by Django 5.0.6 on 2024-05-19 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_alter_tests_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtest',
            name='image',
            field=models.ImageField(upload_to='images/lessons'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(upload_to='images/lessons'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('question', models.TextField(verbose_name='Ответ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
    ]
