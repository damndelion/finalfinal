# Generated by Django 4.1.7 on 2023-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0010_merge_20230511_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(default='1-3.jpg', upload_to='restaurant_img/'),
            preserve_default=False,
        ),
    ]