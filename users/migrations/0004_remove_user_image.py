# Generated by Django 3.2.7 on 2021-10-11 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_face_embedding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
