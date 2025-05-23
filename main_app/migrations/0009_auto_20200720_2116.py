# Generated by Django 3.0.5 on 2020-07-20 19:16

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200715_1250'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', main_app.models.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
