from django.db import IntegrityError

from main_app.models import AnswerReview, Answer


def like(request):
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
