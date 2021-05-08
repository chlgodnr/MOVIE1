from django.shortcuts import render
from django.http import HttpResponse
from .models import Current


def index(request):
    current_list = Current.objects.all()
    context = {'current_list' : current_list}
    return render(request, 'movie/current_list.html', context)