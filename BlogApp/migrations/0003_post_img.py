# Generated by Django 3.2.9 on 2021-11-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_auto_20211116_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
