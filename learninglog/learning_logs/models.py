from django.db import models

class Topic(models.Model):
    '''Um assunto sobre o qual o usuário está aprendendo'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''Vai ser usado para mostrar no painel administrativo'''
        return self.text
    
class Entry(models.Model):
    '''Algo específico aprendido sobre um assunto'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries' #Para o Django saber qual vai ser o plural de Entry
    
    def __str__(self):
        '''Devolve uma representação em string do modelo'''
        return self.text[:50] + '...'
    
