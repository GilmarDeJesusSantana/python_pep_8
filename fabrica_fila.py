from typing import Union

from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[Filanormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return Filanormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe.')
