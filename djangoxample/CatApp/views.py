from django.shortcuts import render
from django.http import HttpResponse

from CatApp.models import Human


# Create your views here.
def home(requests):
    context = {}
    user = Human.objects.first()
    context['name'] =user.name
    context['age'] = user.age
    print(context)
    return render(requests, 'index.html', context)
