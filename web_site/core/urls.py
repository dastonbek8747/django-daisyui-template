from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('kirish/', views.kirish, name='kirish'),
    path('royhatdanotish/', views.royhatdan_otish, name='royhatdan_otish'),
    path('', views.index, name='index'),
]
