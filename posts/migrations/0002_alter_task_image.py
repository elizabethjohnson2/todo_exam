# Generated by Django 4.2.1 on 2023-05-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.FileField(upload_to='tasks/'),
        ),
    ]
