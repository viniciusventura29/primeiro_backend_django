from django.shortcuts import render

# Create your views here.
from home.models import Agenda


def index(request):
    dados = Agenda.objects.order_by(
        '-id'
    )
    context={
        'agenda':dados
    }
    return render(request,'home/index.html',context)