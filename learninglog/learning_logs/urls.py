from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),# Quando acessar '/', chame a função index() do arquivo views.py
    path('topics/', views.topics, name='topics')
]
