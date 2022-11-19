from django.db import models
from django.contrib.auth.models import User
from itertools import cycle




class Dia(models.Model):
    OPCOES:list = [
        (1,'Neutro'),
        (2,'Passado'),
        (3,'Perdido'),
    ]
    estado = models.CharField(
        choices=OPCOES,
        max_length=7,
        editable=True, 
        default=OPCOES[0][0],#iniciando o valor default com a primeira opcao (Neutro)
    )

    class Meta:
        verbose_name = ("Dia")
    def __str__(self):
        return self.estado
    
    def alterar_proximo_estado(self) -> str:
        if int(self.estado) == self.OPCOES[len(self.OPCOES)-1][0]:#se for igual a ultima chave de identificação
            self.estado = str(1) #retorna para o primeiro estado (ciclo)
            return self.estado #retornando o valor do estado
        self.estado = str(int(self.estado) + 1) #caso não seja a ultima, some +1
        return self.estado #retornando o valor do estado

class Setembro(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='dias')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
