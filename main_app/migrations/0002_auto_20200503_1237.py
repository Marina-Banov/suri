# Generated by Django 3.0.5 on 2020-05-03 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='answer',
            name='likes_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answerreview',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Answer'),
        ),
        migrations.AlterField(
            model_name='answerreview',
            name='review',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='answerreview',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='field_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Group'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
