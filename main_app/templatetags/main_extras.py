from django import template
register = template.Library()


@register.filter
def review(things, r):
    return things.filter(review=r)


@register.filter
def user(things, u):
    return things.filter(user=u)
