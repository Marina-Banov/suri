from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('<int:question_id>/', views.question, name='question'),
    path('groups/<int:group_id>/', views.groups, name='groups'),
    path('ask_question/<int:group_id>/', login_required(views.AskQuestion.as_view()), name='ask_question'),
    path('answer/', views.AnswerView.as_view(), name='answer'),
]
