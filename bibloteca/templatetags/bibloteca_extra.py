from django import template
from .. import models
from django.http import HttpResponse

register = template.Library()

@register.filter(name='percentage')
def percentage(currentPages, numPages ):
    return round((currentPages * 100) / numPages )

@register.filter(name='getcurrentstatus')
def getCurrentStatus(status_id):
    return models.Statu.objects.only('descriptions').filter(id = status_id).first()

@register.filter(name='getcurrentpage')
def getCurrentPage(book_id , user_id):
    return models.Progress.objects.values_list('currentPage', flat=True).filter(book = book_id , user = user_id).first()