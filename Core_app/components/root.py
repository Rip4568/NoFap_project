from django_unicorn.components import UnicornView, QuerySetType
from ..models import Setembro, Dia
from django.contrib.auth.models import User
from datetime import datetime

class RootView(UnicornView):
    estado_botao:bool = False
    eh_setembro_root:bool = datetime.now().month == 9
    setembro_root:Setembro = Setembro.objects.none()
    usuario:User

    def testar_objeto(self, objeto):
        print(objeto)

    def alteranar_estado_dia(self, dia:int):
        dia_buscado = Dia.objects.get(dia=dia, mes=self.setembro_root)
        dia_buscado.alterar_proximo_estado()
        dia_buscado.save()