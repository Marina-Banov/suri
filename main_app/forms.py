from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import User, Question, Answer, Group


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ('field_name', 'group_name')


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'image')


class AnswerForm(BSModalForm):

    class Meta:
        model = Answer
        fields = ('description', 'image')
