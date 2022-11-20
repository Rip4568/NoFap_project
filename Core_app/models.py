from django.db import models
from django.contrib.auth.models import User
from itertools import cycle

class Setembro(models.Model):
    # dia = models.ForeignKey(Dia, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User', blank=True, null=True)

    def __str__(self):
        return f'{self.usuario}'
class Dia(models.Model):
    OPCOES:list = [
        ('N','Neutro'),
        ('P','Passado'),
        ('F','Perdido'),
    ]
    dia = models.PositiveIntegerField(default=0)
    mes = models.ForeignKey(Setembro, on_delete=models.CASCADE, related_name='dias', blank=True, null=True)
    estado = models.CharField(
        choices=OPCOES,
        max_length=7,
        editable=True, 
        default=OPCOES[0],#iniciando o valor default com a primeira opcao (Neutro)
    )

    class Meta:
        verbose_name = ("Dia")
    def __str__(self):
        return self.estado[0]
    
    def alterar_proximo_estado(self) -> str:
        if self.estado == 'N':
            self.estado = 'P'
        elif self.estado == 'P':
            self.estado = 'F'
        else:
            self.estado = 'N'
        pass

class SETEMBRO_GERAL(models.Model):
    CHEGOU_SETEMBRO = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.CHEGOU_SETEMBRO}'