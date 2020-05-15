from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import User, Question, Answer


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'image')


class AnswerForm(BSModalForm):

    class Meta:
        model = Answer
        fields = ('description', 'image')
