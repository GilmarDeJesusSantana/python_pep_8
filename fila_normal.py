

from fila_base import FilaBase


class Filanormal(FilaBase):
    def gerasenhaatual(self) -> None:
        self.senha_atualatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerasenhaatual()
        self.fila.append(self.senha_atual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
