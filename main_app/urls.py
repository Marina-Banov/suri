from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('edit_profile/', views.update_profile, name='edit_profile'),
    path('password/', login_required(views.MyPasswordChangeView.as_view()), name='change_password'),
    path('group/<int:group_id>/', views.group, name='group'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('create_group/', login_required(views.CreateGroupView.as_view()), name='create_group'),
    path('accept_group/<int:group_id>/<int:notif_id>', views.accept_group, name='accept_group'),
    path('deny_group/<int:group_id>/<int:notif_id>', views.deny_group, name='deny_group'),
    path('create_question/<int:group_id>/', login_required(views.CreateQuestionView.as_view()), name='create_question'),
    path('create_answer/<int:question_id>/', login_required(views.CreateAnswerView.as_view()), name='create_answer'),
    path('delete_group/<int:pk>', login_required(views.DeleteGroupView.as_view()), name='delete_group'),
    path('delete_question/<int:pk>/', login_required(views.DeleteQuestionView.as_view()), name='delete_question'),
    path('delete_answer/<int:pk>/', login_required(views.DeleteAnswerView.as_view()), name='delete_answer')
]
