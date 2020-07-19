from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('group/<int:group_id>/', views.group, name='group'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('create_question/<int:group_id>/', login_required(views.CreateQuestionView.as_view()), name='create_question'),
    path('create_group/', login_required(views.CreateGroupView.as_view()), name='create_group'),
    path('delete_question/<int:pk>/', views.DeleteQuestionView.as_view(), name='delete_question'),
    path('create_answer/<int:question_id>/', views.CreateAnswerView.as_view(), name='create_answer'),
    path('delete_answer/<int:pk>/', views.DeleteAnswerView.as_view(), name='delete_answer'),
    path('delete_group/<int:pk>', views.DeleteGroupView.as_view(), name='delete_group')
]
