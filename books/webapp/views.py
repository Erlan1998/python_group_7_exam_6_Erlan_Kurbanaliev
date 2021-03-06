from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guest, status_choices
# Create your views here.

def index_view(request):
    guest = Guest.objects.all().filter(status='active').order_by('date_creat')
    return render(request, 'index.html', context={'guests': guest})

