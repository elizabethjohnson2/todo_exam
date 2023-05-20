# Generated by Django 4.2.1 on 2023-05-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_task_delete_image_task_edit_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_edit', models.BooleanField(default=False)),
            ],
        ),
    ]
