# Generated by Django 5.0 on 2023-12-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.CharField(max_length=200)),
                ('v_email', models.EmailField(max_length=254)),
                ('v_messege', models.TextField()),
            ],
        ),
    ]
