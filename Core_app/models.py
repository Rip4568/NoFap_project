from django.db import models

class Dia(models.Model):
    estado = models.CharField(
        choices=[
            (1,'Neutro'),
            (2,'Passado'),
            (3,'Perdido'),
        ],
        max_length=7,
        editable=True, 
        default='Neutro',
    )

    class Meta:
        verbose_name = ("Dia")
    def __str__(self):
        return self.estado
    