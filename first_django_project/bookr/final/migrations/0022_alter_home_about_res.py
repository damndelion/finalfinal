# Generated by Django 4.2 on 2023-05-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0021_alter_home_about_img_alter_home_img_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='about_res',
            field=models.CharField(help_text='res about', max_length=10000),
        ),
    ]