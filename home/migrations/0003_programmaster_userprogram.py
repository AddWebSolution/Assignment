# Generated by Django 4.1.2 on 2022-10-10 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_usermaster_is_active_usermaster_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.CharField(choices=[(None, 'Select'), ('R', 'R'), ('W', 'W'), ('B', 'B')], default=None, max_length=2)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.programmaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]