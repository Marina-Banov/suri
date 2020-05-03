from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    subscribers = models.ManyToManyField(get_user_model(), related_name='subscribers')
    admin = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='admin', null=True)

    def __str__(self):
        return self.group_name + ', ' + self.field_name


class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2048, null=True)
    # the images themselves aren't saved to the database, just the pathway to the image
    # the images are stored in the media directory of the project
    image = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=2048)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    accepted = models.BooleanField(default=False)
    likes_count = models.IntegerField(null=True)
    dislikes_count = models.IntegerField(null=True)

    def __str__(self):
        return self.question.title + ': ' + self.description


class AnswerReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    review = models.IntegerField()
