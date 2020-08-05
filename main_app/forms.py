from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, BooleanField
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import User, Question, Answer, Group


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'university', 'image')


class GroupForm(ModelForm):

    admin_check = BooleanField(required=False)

    class Meta:
        model = Group
        fields = ('field_name', 'group_name') + ('admin_check',)


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'image')


class AnswerForm(BSModalModelForm):

    class Meta:
        model = Answer
        fields = ('description', 'image')
