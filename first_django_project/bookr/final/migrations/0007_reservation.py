# Generated by Django 4.1.7 on 2023-05-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0006_delete_examplemodel_book_cover_book_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(help_text='Username', max_length=40)),
                ('Name', models.CharField(help_text="Username's name", max_length=40)),
                ('Email', models.CharField(help_text='Enmail-address', max_length=50)),
                ('Phone_num', models.CharField(help_text='Phone number', max_length=50)),
                ('Number', models.IntegerField(help_text='Number of guests')),
                ('Date', models.DateField(help_text='Date of reservation')),
                ('Time', models.CharField(help_text='Time', max_length=30)),
                ('Message', models.TextField(max_length=200)),
            ],
        ),
    ]
