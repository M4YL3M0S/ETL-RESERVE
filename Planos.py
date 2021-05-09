class Planos (object):

    def __init__(self,id, nome, favorecido, datainicio, datafim, tipo, status, moeda,
                 totalPlanejado, totalDeDespesas ):
        self.id = id
        self.nome = nome
        self.favorecido = favorecido
        self.datainicio = datainicio
        self.datafim = datafim
        self.tipo = tipo
        self.status = status
        self.moeda = moeda
        self.totalPlanejado = totalPlanejado
        self.totalDeDespesas = totalDeDespesas

    def as_list(self):
        return [self.id, self.nome, self.favorecido, self.datainicio, self.datafim, self.tipo,
                self.status, self.moeda, self.totalPlanejado, self.totalDeDespesas]