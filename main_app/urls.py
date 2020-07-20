from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('edit_profile/', views.update_profile, name='edit_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'), # template_name='registration/reset-password.html'
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('group/<int:group_id>/', views.group, name='group'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('create_group/', login_required(views.CreateGroupView.as_view()), name='create_group'),
    path('create_question/<int:group_id>/', login_required(views.CreateQuestionView.as_view()), name='create_question'),
    path('create_answer/<int:question_id>/', login_required(views.CreateAnswerView.as_view()), name='create_answer'),
    path('delete_group/<int:pk>', login_required(views.DeleteGroupView.as_view()), name='delete_group'),
    path('delete_question/<int:pk>/', login_required(views.DeleteQuestionView.as_view()), name='delete_question'),
    path('delete_answer/<int:pk>/', login_required(views.DeleteAnswerView.as_view()), name='delete_answer')
]
