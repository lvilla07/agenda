from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # max_length defini o tamanho total que o campo pode receber
    descricao = models.TextField(blank=True, null=True) # o parametro blank permite que o campo seja em branco e o campo null permite que o campo seja nulo, por default ambos vem como False
    local = models.CharField(max_length=100, blank=True, null=True) # o parametro blank permite que o campo seja em branco e o campo null permite que o campo seja nulo, por default ambos vem como False
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #verbose_name é uma config do alias que será aberto dessa coluna quando aberto no django admin
    data_criacao = models.DateTimeField(auto_now=True) #Auto_now True significa q sempre q criado um registro ele loja data e hora atual e salva
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete faz com que se o usuario desse evento for deletado o evento tambem seja

    class Meta: #serve para nomear a tabela
        db_table = 'evento'

    def __str__(self): #Defini que o nome dado ao Evento seja o nome exibido nele mesmo quando aberto no django admin
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Horas')

    def get_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
        # foi necessario criar esse input para retornar uma string ao
        # retornar o mesmo quando editado um evento, esse '%Y-%m-%dT%H:%M'
        # é o padrão que os navegadores entendem.

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
