from django.urls import path
from . import views 

urlpatterns = [
    path('status/<int:status_id>' , views.index , name='index'),
]
