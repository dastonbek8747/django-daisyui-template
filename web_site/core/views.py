from django.shortcuts import render
from . import models


def index(request):
    test = models.Test.objects.all()
    return render(request, 'index.html', {'ctg': test})
