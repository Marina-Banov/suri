from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from main_app.forms import CustomUserCreationForm
from main_app.models import Group, Question, Answer


def index(request):
    all_groups = Group.objects.all()
    context = {'all_groups': all_groups}
    return render(request, 'main_app/index.html', context)


def question(request, question_id):
    q = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question_id=question_id)
    context = {
        'question': q,
        'answers': answers
    }
    return render(request, 'main_app/questions.html', context)


def groups(request, group_id):
    group = Group.objects.get(id=group_id)
    questions = Question.objects.filter(group=group_id)
    context = {
        'group': group,
        'questions': questions
    }
    return render(request, 'main_app/groups.html', context)


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('index'))
