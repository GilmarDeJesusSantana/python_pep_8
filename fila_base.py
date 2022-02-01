from abc import ABCMeta, abstractmethod


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ''

    def reseta_fila(self):
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    @abstractmethod
    def gera_senha_atual(self):
        ...

    @abstractmethod
    def atualiza_fila(self):
        ...

    @abstractmethod
    def chama_cliente(self, caixa: int):
        ...
