# Generated by Django 4.1.2 on 2022-10-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_programmaster_userprogram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprogram',
            name='program',
        ),
        migrations.AddField(
            model_name='userprogram',
            name='program',
            field=models.ManyToManyField(blank=True, to='home.programmaster'),
        ),
    ]