# Generated by Django 4.1.2 on 2022-10-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usermaster',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
