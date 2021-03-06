from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guest, status_choices
from webapp.forms import GuestForm
# Create your views here.

def index_view(request):
    guest = Guest.objects.all().filter(status='active').order_by('date_creat')
    return render(request, 'index.html', context={'guests': guest})


def guest_add_view(request):
    if request.method == 'GET':
        guest = GuestForm()
        return render(request, 'add_guest.html', context={'form': guest})
    elif request.method == 'POST':
        guest = GuestForm(data=request.POST)
        if guest.is_valid():
            guest = Guest.objects.create(
                name=guest.cleaned_data.get('name'),
                mail=guest.cleaned_data.get('mail'),
                description=guest.cleaned_data.get('description')
            )
            return redirect('index_all')
        return render(request, 'add_guest.html', context={'guest': guest})


def guest_update_view(request, id):
    guest = get_object_or_404(Guest, id=id)
    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest.name,
            'mail': guest.mail,
            'description': guest.description
        })
        return render(request, 'update.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = request.POST.get('name')
            guest.mail = request.POST.get('mail')
            guest.description = request.POST.get('description')
            guest.save()
            return redirect('index_all')
        return render(request, 'add_guest.html', context={'form': form, 'guest': guest})


def guest_delete_view(request, id):
    guest = get_object_or_404(Guest, id=id)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
    return redirect('index_all')
