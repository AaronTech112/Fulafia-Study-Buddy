# Generated by Django 4.1 on 2022-10-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_message_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='body_image',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]