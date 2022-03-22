from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# there two types of views functions/class based

def taskList(request):
    return HttpResponse('Our 4PM to do list')