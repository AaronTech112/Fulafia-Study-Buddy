# Generated by Django 4.1 on 2022-10-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body_image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]