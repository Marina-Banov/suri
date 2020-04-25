from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    def __str__(self):
    	return self.group_name + ', ' + self.field_name

class UserGroup(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Question(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	date = models.DateTimeField()
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1024)
	def __str__(self):
		return self.title + ': ' + self.description

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	date = models.DateTimeField()
	description = models.CharField(max_length=1024)
	accepted = models.BooleanField()
	likes_count = models.IntegerField()
	dislikes_count = models.IntegerField()
	def __str__(self):
		return self.description

class AnswerReview(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	review = models.IntegerField()