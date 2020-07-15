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
    approved = models.BooleanField()

    def __str__(self):
        return self.group_name + ', ' + self.field_name


class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2048, null=True)
    # the images themselves aren't saved to the database, just the pathway to the image
    # the images are stored in the media directory of the project
    image = models.FileField(upload_to='images/', null=True, blank=True, verbose_name='')
    accepted_answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True, related_name='accepted_answer')

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=2048)
    image = models.FileField(upload_to='images/', null=True, blank=True, verbose_name='')

    @property
    def likes_count(self):
        return AnswerReview.objects.filter(answer=self, review=1).count()

    @property
    def dislikes_count(self):
        return AnswerReview.objects.filter(answer=self, review=-1).count()

    def __str__(self):
        return self.question.title + ': ' + self.description


class AnswerReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='user_like_key', null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_like_key')
    review = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'answer'], name='uniqueAnswerReview')
        ]

    def __str__(self):
        return str(self.user) + (' liked ' if (self.review == 1) else ' disliked ') + str(self.answer)
