class Filanormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhatual:str = ''

    def gerasenhaatual(self)-> None:
        self.senhatual = f'NM{self.codigo}'
