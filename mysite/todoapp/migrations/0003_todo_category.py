# Generated by Django 3.1.1 on 2020-10-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.CharField(default='None', max_length=20),
        ),
    ]