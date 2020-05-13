from django import template
from .. import models
register = template.Library()

@register.filter(name='percentage')
def percentage(currentPages, numPages ):
    return round((currentPages * 100) / numPages )

@register.filter(name='getcurrentstatus')
def getCurrentStatus(status_id):
    return models.Statu.objects.only('descriptions').filter(id = status_id).first()