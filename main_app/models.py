from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Group(models.Model):
    group_name = models.CharField(max_length=50, null=True)
    field_name = models.CharField(max_length=50, null=True)
    subscribers = models.ManyToManyField(get_user_model(), related_name='subscribers')
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='admin', null=True)

    def __str__(self):
        return self.group_name + ', ' + self.field_name


class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return self.title + ': ' + self.description


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    description = models.CharField(max_length=1024, null=True)
    accepted = models.BooleanField(null=True)
    likes_count = models.SmallIntegerField(null=True)
    dislikes_count = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class AnswerReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    review = models.IntegerField(null=True)
