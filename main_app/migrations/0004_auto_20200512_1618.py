# Generated by Django 3.0.5 on 2020-05-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200509_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name=''),
        ),
    ]
