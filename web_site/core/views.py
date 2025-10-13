from django.shortcuts import render
from . import models


def index(request):
    test = models.Test.objects.all()
    return render(request, 'index.html', {'ctg': test})


def about(request):
    test = models.Test.objects.all()
    return render(request, 'about.html', {'ctg': test})


def contact(request):
    test = models.Test.objects.all()
    return render(request, 'contact.html', {'ctg': test})


def kirish(request):
    test = models.Test.objects.all()
    return render(request, 'auth/kirish.html', {'ctg': test})


def royhatdan_otish(request):
    test = models.Test.objects.all()
    return render(request, 'auth/royhatdan_otish.html', {'ctg': test})


def test(request):
    test = models.Test.objects.all()
    return render(request, 'test.html', {'ctg': test})
