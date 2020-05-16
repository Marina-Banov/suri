from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from main_app.forms import CustomUserCreationForm, QuestionForm, AnswerForm
from main_app.models import Group, Question, Answer, AnswerReview


def index(request):
    context = {
        'all_groups': Group.objects.all()
    }
    return render(request, 'main_app/index.html', context)


def group(request, group_id):
    context = {
        'group': Group.objects.get(id=group_id),
        'questions': Question.objects.filter(group=group_id)
    }
    return render(request, 'main_app/group.html', context)


def question(request, question_id):
    if request.method == 'POST':
        r = AnswerReview()
        r.user = request.user
        r.answer = Answer.objects.get(id=request.POST.get('answer'))
        if 'like' in request.POST:
            r.review = 1
        else:
            r.review = -1
        try:
            r.save()
        except IntegrityError:
            AnswerReview.objects.get(user=r.user, answer=r.answer).delete()

    context = {
        'question': Question.objects.get(id=question_id),
        'answers': Answer.objects.filter(question_id=question_id)
    }
    return render(request, 'main_app/question.html', context)


class CreateQuestionView(generic.CreateView):
    form_class = QuestionForm
    template_name = 'main_app/create_question.html'

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


class CreateAnswerView(BSModalCreateView):
    form_class = AnswerForm
    template_name = 'main_app/create_answer.html'

    def form_valid(self, form):
        a = Answer(
            question=Question.objects.get(id=self.kwargs['question_id']),
            user=self.request.user,
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image']
        )
        a.save()    # TODO saves answer twice???
        return HttpResponseRedirect(reverse('question', kwargs={'question_id': a.question.id}))


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
