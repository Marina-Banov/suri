from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main_app/index.html')


def question(request, question_id):
    return HttpResponse("Question %s" % question_id)
