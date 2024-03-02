from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import DetailView

from .models import Fast

from .forms import FastForm
# Create your views here.

class FastDetailView(DetailView):
    model = Fast
    template_name = 'main/fast.html'
    context_object_name = 'fast'


def index(request):
    fasts = Fast.objects.all()

    return render(
        request,'main/index.html', {'fasts' : fasts})

def create(request):
    form = FastForm()
    error = ''
    if request.method == 'POST':
        form = FastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Неверно'

    data = {
        'form': form,
        'error':error
    }


    return render(
        request,
        'main/create.html',
        data)

def leave(request):
    return (render(
        request=request,
        template_name='main/leave.html'))

def join(request):
    return (render(
        request=request,
        template_name='main/join.html'))
