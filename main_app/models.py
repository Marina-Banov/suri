from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    def __str__(self):
        return self.group_name + ', ' + self.field_name

class UserGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1024, null=True)
    def __str__(self):
        return self.title + ': ' + self.description

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    description = models.CharField(max_length=1024, null=True)
    accepted = models.BooleanField(null=True)
    likes_count = models.SmallIntegerField(null=True)
    dislikes_count = models.IntegerField(null=True)
    def __str__(self):
        return self.description

class AnswerReview(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    review = models.IntegerField(null=True)