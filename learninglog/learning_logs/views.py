from django.shortcuts import render
from .models import Topic

def index(request):
    '''Página principal do learning_log
     A função index pega o request e retorna a página index.html que está na pasta learning_logs/templates/learning_logs.
    '''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Mostra os tópicos
    Vai ser necessário ter um dicionário (context) para ser renderizado na página, nesse caso a chave vai ser Topics. O context vai ser passado através do return 
    '''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics} 
    return render(request, 'learning_logs/topics.html', context)