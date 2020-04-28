from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User


admin.site.register(User, Admin)
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerReview)
