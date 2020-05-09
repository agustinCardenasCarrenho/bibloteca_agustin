from django.shortcuts import render
from django.http import HttpResponse
from .models import Statu

def index(request):
    status = Statu.objects.all()
    return HttpResponse(status)
