from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    '''Página principal do learning_log
     A função index pega o request e retorna a página index.html que está na pasta learning_logs/templates/learning_logs.
    '''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Mostra os tópicos
    Vai ser necessário ter um dicionário (context) para ser renderizado na página, nesse caso a chave vai ser Topics. O context vai ser passado através do return 
    '''
    topics = Topic.objects.order_by('date_added') #Ordenado pelo parâmetro de data
    context = {'topics': topics} #Para ser renderizado precisa ser um dict
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''Mostra um único assunto e todas as suas entradas'''
    topic = Topic.objects.get(id = topic_id) #vai retornar o que tiver no banco com esse id
    entries = topic.entry_set.order_by('-date_added') #entry_set traz todos os entries associados ao tópico
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''Adiciona um novo tópico'''
    if request.method != 'POST':
        #Nenhum dado submetido, cria um formulário em branco
        form = TopicForm()
    else:
        #Dados de post submetidos; processa os dados
        form = TopicForm(request.POST) #Recebe os dados do envio do formulário
        if form.is_valid(): #Valida os dados inseridos
            form.save() #Salva no banco de dados
            return HttpResponseRedirect(reverse('topics'))   #utiliza o nome da página lá de urls
    
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''Acrescente uma nova entrada para um tópico em particular'''
    topic = Topic.objects.get(id = topic_id) #Para identificar o tópico
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST) #não ser pego apenas o data da requisição por enquanto
        if form.is_valid(): #Valida os dados inseridos
                new_entry = form.save(commit=False) #commit false vai fazer com que não salve no banco ainda
                new_entry.topic = form #Agora sim vai ser adicionado o tópico da nova entrada
                new_entry.save() #Salva no banco de dados
                return HttpResponseRedirect(reverse('topics', args=[topic_id]))#Vai redirecionar para o tópico em específico
    
    context = {'topic': topic, 'form': form} #Senão entrar no else, vai ser executado essa linha
    return render(request,'learning_logs/new_entry.html', context)
