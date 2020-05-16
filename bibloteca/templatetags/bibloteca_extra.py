from django import template
from .. import models
from django.http import HttpResponse

register = template.Library()

@register.filter(name='percentage')
def percentage(currentPages, numPages ):
    return round((currentPages * 100) / numPages )

@register.filter(name='getcurrentstatusdescriptions')
def getCurrentStatus(book_id, user_id):
    return models.State.objects.values_list('statu__descriptions' , flat=True).filter(book = book_id , user = user_id).first()

@register.filter(name='getcurrentstatusid')
def getCurrentStatus(book_id, user_id):
    return models.State.objects.values_list('statu__id' , flat=True).filter(book = book_id , user = user_id).first()

@register.filter(name='getcurrentpage')
def getCurrentPage(book_id , user_id):
    return models.Progress.objects.values_list('currentPage', flat=True).filter(book = book_id , user = user_id).first()