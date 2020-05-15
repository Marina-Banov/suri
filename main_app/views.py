from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from main_app.forms import CustomUserCreationForm, QuestionForm, AnswerForm
from main_app.views_helpers import like
from main_app.models import Group, Question, Answer


def index(request):
    all_groups = Group.objects.all()
    context = {'all_groups': all_groups}
    return render(request, 'main_app/index.html', context)


def question(request, question_id):
    """
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            print(1)
        elif request.POST.get("form_type") == 'formTwo':
            print(2)
    """
    if request.method == 'POST':
        like(request)

    context = {
        'question': Question.objects.get(id=question_id),
        'answers': Answer.objects.filter(question_id=question_id)
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


class AskQuestion(generic.CreateView):
    form_class = QuestionForm
    template_name = 'main_app/ask_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = Group.objects.get(id=self.kwargs['group_id']),
        return context

    def form_valid(self, form):
        b = Question(
            group=Group.objects.get(id=self.kwargs['group_id']),
            user=self.request.user,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image']
        )
        b.save()
        return HttpResponseRedirect(reverse('question', kwargs={'question_id': b.id}))


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.request.POST.get('next', '/'))


class AnswerView(BSModalCreateView):
    template_name = 'main_app/give_answer.html'
    form_class = AnswerForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')