from django.contrib import admin

from .models import *

admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerReview)
