# Generated by Django 4.2.1 on 2023-05-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_delete_completed_task_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_revised',
            field=models.BooleanField(default=False),
        ),
    ]