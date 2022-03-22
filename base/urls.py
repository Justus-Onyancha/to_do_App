
# this is urls we made for our base app
from django.urls import path

from . import views

urlpatterns = [
   path('', views.taskList, name='base')
]


