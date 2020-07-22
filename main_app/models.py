from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    university = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to='images/', blank=True, verbose_name='')
    objects = CustomUserManager()

    @property
    def questions_asked(self):
        return Question.objects.filter(user=self).count()

    @property
    def answers_count(self):
        return Answer.objects.filter(user=self).count()

    @property
    def accepted_count(self):
        answers = Answer.objects.filter(user=self)
        accepted = 0
        for a in answers:
            try:
                Question.objects.get(accepted_answer=a)
                accepted += 1
            except Question.DoesNotExist:
                continue
        return accepted

    @property
    def likes_count(self):
        answers = Answer.objects.filter(user=self)
        return sum(a.likes_count for a in answers)

    def __str__(self):
        return self.username


class Group(models.Model):
    class Fields(models.TextChoices):
        MAT = "Matematika"
        FIZ = "Fizika"
        KEM = "Kemija"
        BIO = "Biologija"
        ARH = "Arhitektura"
        BROD = "Brodogradnja"
        ET = "Elektrotehnika"
        GRAD = "Građevinarstvo"
        KEM_INZ = "Kemijsko inženjerstvo"
        RAC = "Računarstvo"
        STR = "Strojarstvo"
        TEH_PROM = "Tehnologija prometa"
        MED = "Medicina"
        VET = "Veterina"
        DENT = "Dentalna medicina"
        FARM = "Farmacija"
        BT = "Biotehnologija"
        PT = "Prehrambena tehnologija"

    group_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50, choices=Fields.choices)
    subscribers = models.ManyToManyField(get_user_model(), related_name='subscribers')
    admin = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='admin', null=True)
    approved = models.BooleanField()

    @property
    def posts_count(self):
        return Question.objects.filter(group=self).count()

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
